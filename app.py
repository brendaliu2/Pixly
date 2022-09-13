# FLASK IMPORTS
from flask import Flask, render_template, redirect, flash, request

# MODEL IMPORTS 
# from models import db, connect_db, User, Post

#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# TODO: DB imports and setup
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)

# app.config['SECRET_KEY'] = "SECRET!"
# #debug = DebugToolbarExtension(app)

# db.create_all()


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

# @app.post('/users/new')
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