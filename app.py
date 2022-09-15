# FLASK IMPORTS
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request
from boto_model import  upload_file
from werkzeug.utils import secure_filename
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import uuid
from filters import *
from PIL import Image, ImageOps, ImagePalette
from urllib.request import urlopen
from sqlalchemy import update

import io
import base64


load_dotenv()

# MODEL IMPORTS 
from models import db, connect_db, UserImage

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pixly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['ACCESS_KEY'] = os.environ['ACCESS_KEY']
app.config['SECRET_ACCESS_KEY'] = os.environ['SECRET_ACCESS_KEY']
app.config['BUCKET'] = os.environ['BUCKET']

BUCKET = os.environ['BUCKET']
BASE_URL = os.environ['BASE_URL']

connect_db(app)

# app.config['SECRET_KEY'] = "SECRET!"
#debug = DebugToolbarExtension(app)

db.create_all()


##################### UTILITY FUNCTIONS ##################### 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_unique_filename(filename):
    file_uuid = str(uuid.uuid4())
    file_extension = filename.rsplit('.', 1)[1].lower()
    return f"{file_uuid}.{file_extension}"

# TODO: How to get EXIF data into database?
def get_exif_data(image):
    img = Image.open(image)
    img.load()
    img_exif = img.getexif()
    
    if img_exif is None:
        return None
    else:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
        
    return

def set_filter(file, filter):
    if filter == 'gray':
            img = gray(file)
    elif filter == 'sepia':
            img = sepia(file)
    elif filter == 'border':
            img = border(file)
    elif filter == 'resize':
            img = resize(file)
    elif filter == 'random':
            img = random(file)
    else: 
            return file
        
    return img


##################### ROUTES ##################### 

# HOMEPAGE (accept filter parameter)
# One button for search, one button for upload

# EDIT PAGE 
# Filter buttons, submit button
# Redirect to homepage

# SEARCH FORM (redirect to homepage)

##################### HOMEPAGE ##################### 
@app.get('/')
def show_images():
    """
    Show all images.
    Each image is a link to route for show_image based on the target's primary key.

    """
    
    hasSearch = request.args
    
    if hasSearch:
        searchTerm = request.args['search'].lower()
        #TODO: how to filter by multiple different values?
        all_images = UserImage.query.filter(
            UserImage.description.like(f"%{searchTerm}%"),
            UserImage.published == True).all()

    else:
        all_images = UserImage.query.filter(
            UserImage.published == True).all()

    img_urls = []
    
    for image in all_images:
        img_urls.append(f'{BASE_URL}{image.filename}')
        
    return render_template('image_listing.html', all_images = img_urls)


##################### SEARCH ##################### 

@app.get('/search')
def show_search_form():
    """
    Show form with one input for image search

    """
    #flask wtf form
    
    return render_template('search_form.html')
    
    
##################### UPLOAD ##################### 
@app.get('/upload')
def show_upload_form():
    """
    Show upload form

    """
    return render_template('upload_form.html')
    


@app.post('/upload')
def process_upload_form():
    """
    Upload image to DB, upload to AWS, redirect to edit page 
    """
    
    file = request.files['file'] 
    extra_args = {'ContentType': file.content_type, 'ACL': 'public-read'}

    #getting exif tag
    #get_exif_data(file)

    if file.filename == '':
        return redirect('/')
        
    if file and allowed_file(file.filename):

        unique_filename = generate_unique_filename(file.filename)
        filename = secure_filename(unique_filename)
        
        #add to AWS
        upload_file(file, BUCKET, filename, extra_args)
        #TODO: manipulate 'published' at later point
        
        #add to DB
        #TODO: Set original image to be published=False once edit form is running
        new_image = UserImage(filename=filename,published=False,content_type=file.content_type)
        db.session.add(new_image)
        db.session.commit()
        return redirect(f'edit/{filename}')
        
    return redirect('/')
    

##################### EDIT ##################### 
# @app.post('/edit')
# def process_edit():
    '''
    Change photo to gray, sepia, size, border depending on user selection
    '''
    #accept form selection
    
    # edit filter helper function
    
    
    #upload to AWS
    
    #redirect ('edit_form')
    
@app.get('/edit/<filename>')
def display_edit(filename):
    '''
    Diplay original photo, edited photo result(if applicable), and form to edit
    '''
    
    og_image = f'{BASE_URL}{filename}'
    
    try:
        filter = request.args['filter']
        data = set_filter(urlopen(og_image), filter)
        encoded_img_data = base64.b64encode(data.getvalue())
        new_image = encoded_img_data.decode('utf-8')
    except:
        filter = 'none'
        new_image = None
    
    return render_template(
        'edit_page.html', 
        og_image=og_image, 
        filename=filename,
        filter=filter,
        encoded_image=new_image
        )
    
@app.post('/edit/<filename>/<filter>')
def publish_edit(filename, filter):
    '''
    Uploads edited photo to AWS and returns to homepage
    '''
    og_image = f'{BASE_URL}{filename}'
    og_file = UserImage.query.get(filename)
    
    description = request.form['description']
    
    try:
        data = set_filter(urlopen(og_image), filter)
        encoded_img_data = base64.b64encode(data.getvalue())
        new_image = encoded_img_data.decode('utf-8')
    except:
        image = UserImage.query.get(filename)
        image.published = True
        image.description = description
        db.session.commit()
        return redirect('/')
 
 
    #add to AWS
    extra_args = {'ContentType': og_file.content_type, 'ACL': 'public-read'}
    unique_filename = generate_unique_filename(filename)
    edited_filename = secure_filename(unique_filename)
    
    upload_file(data, BUCKET, edited_filename, extra_args)

    edited_image = UserImage(filename=edited_filename, 
                             published=True, 
                             content_type=og_file.content_type, 
                             filter=filter,
                             description=description)
    db.session.add(edited_image)
    db.session.commit()

    return redirect('/')