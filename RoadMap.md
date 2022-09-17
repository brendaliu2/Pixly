Pixly:

Backend: Python with Pillow Library
Frontend: Jinja


Pages:
WORKING - HomePage (displays all images with published as t)
WORKING - Form for adding new photo
WORKING - Search for photo
WORKING - Edit photo


Thing to Research:
-DONE-upload images
-DONE-retrieve metadata from photo(location, camera, etc) & store in AWS/DB
-DONE-store image file in AWS
-DONE Edit photos with Pillow library
-DONE upload photo to AWS 



Database:
    columns:
        * filename (req)
        * published (req)
        * filter (opt)
        * exifdata (holds JSON?)
        * tags ?


User Perspective:
1. Arrive at homepage with photos
2. Click upload photo
3. Editing page with buttons that link pillow commands
4. Click publish



FRIDAY:
DONE- Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)
DONE file clean up, docstrings
    - clean /upload /search routes

- lightning talk plan
    
    
Additional Features: 
    - come back to unfinished photo, search for certain filters
    - flask wtforms
    - more palettes
    - keep random result palette consistent when image is published
    - make buttons swap filters when selected instead of form submit
    - photo/desc as link to display metadata?
    
Lightning:

- Intro:
    B-Tech stack: Flask & Jinja
    E-HomePage 
    E-Demo upload
    E-Demo edit
    E-Demo search

- What we used to build: 
    B- Pillow
        -filters
    E- Bytes IO 
        -not saving to AWS or DB while editing
 
 -Bug Stories
    -Exif Data
        B- opening/closing image file -> BytesIO
        E- datatypes of exif vs datatypes of python dict -> cast helper func
            -Pillow creates other datatype when extracting EXIF

-Version 2 Plans:
    B- Make photos on homepage clickable for detail
    E- More filters
    B- Come back to unfinished photo
    E- Easy download edited photo to user computer at different resolutions
    B- Save palette info of random filter for consistency when published

