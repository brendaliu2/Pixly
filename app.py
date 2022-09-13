# FLASK IMPORTS
import os
from dotenv import load_dotenv
from urllib.parse import urldefrag
from flask import Flask, render_template, redirect, flash, request
from boto_model import  upload_file
from werkzeug.utils import secure_filename
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

load_dotenv()
# MODEL IMPORTS 
# from models import db, connect_db, User, Post

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# TODO: DB imports and setup
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['ACCESS_KEY'] = os.environ['ACCESS_KEY']
app.config['SECRET_ACCESS_KEY'] = os.environ['SECRET_ACCESS_KEY']
app.config['BUCKET'] = os.environ['BUCKET']

BUCKET = os.environ['BUCKET']

# connect_db(app)

# app.config['SECRET_KEY'] = "SECRET!"
# #debug = DebugToolbarExtension(app)

# db.create_all()

TEST_IMAGE_PATH = 'images/test.jpg'


##################### UTILITY FUNCTIONS ##################### 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           

def get_exif_data(image):
    img = Image.open(image)
    img.load()
    img_exif = img.getexif()
    
    if img_exif is None:
        print('Sorry, image has no exif data.')
    else:
        
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
            else:
                print('no keys')
        print('we got here')
        breakpoint()
        

    return
        

##################### ROUTES ##################### 

# HOMEPAGE (accept filter parameter)
# One button for search, one button for upload

# EDIT PAGE 
# Filter buttons, submit button
# Redirect to homepage

# SEARCH FORM (redirect to homepage)


@app.get('/')
def show_images():
    """
    Show all images.
    Each image is a link to route for show_image based on the target's primary key.

    """
    # all_images = Image.query.all()
    all_images = ['a','b','c']

    return render_template('image_listing.html', all_images = all_images)


# @app.get('/search')
# def show_search_form():
#     """
#     Show form with one input for image search

#     """
#     #flask wtf form
    
#     return render_template('search.html', search_form = search_form)
    
    

@app.get('/upload')
def show_upload_form():
    """
    Show upload form

    """
    
    return render_template('upload_form.html')
    

@app.post('/upload')
def process_upload_form():
    """
    Upload image to DB, upload to AWS, redirect homepage 

    """
    
    #uploading to AWS
    file = request.files['file']
    extra_args = {'ContentType': file.content_type, 'ACL': 'public-read'}
    
    
    get_exif_data(file)
    
    if file.filename == '':
        flash('No selected file')
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_file(file, BUCKET, filename, extra_args)
        
        
        
        return redirect('/')
    
    
    #getting exif tag
    
    
    return redirect('/')
    
    #instatiate image instance
    # new_image = Image()
    
    #parse image metadata

    #upload image to AWS & get URL
    #store metadata in DB with models 
    
    
    
# @app.get('/users/new')
# def add_user():
#     """Process the add form, adding a new user and going back to /users"""

#     form_data = request.form
#     first_name = form_data["first_name"]
#     last_name = form_data["last_name"]
#     image_url = form_data["image_url"]

#     #instantiate new user
#     new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)

#     #send user information to database and update
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect('/users')