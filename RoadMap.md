Pixly:

Backend: Python with Pillow Library
Frontend: Jinja...then React if time to spare


Pages:
WORKING - HomePage (displays all images with published as t)
WORKING - Form for adding new photo
WORKING - Search for photo
-Edit photo


Thing to Research:
-DONE-upload images
-DONE-retrieve metadata from photo(location, camera, etc) & store in AWS/DB
-DONE-store image file in AWS
-DONE Edit photos with Pillow library
-DONE upload photo to AWS 

-Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)


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

THURSDAY MORNING:
DONE edit page
- implement tags?

THURSDAY AFTERNOON:
DONE styling

FRIDAY:
- file clean up, docstrings
    - clean /upload /search routes
- lightning talk plan
- photo/desc as link to display metadata?

    
- vscode pretty upgrade??
    
Additional Features: 
    - come back to unfinished photo, search for certain filters
    - flask wtforms
    - more palettes
    - keep random result palette consistent when image is published
    - make buttons swap filters when selected instead of form submit
    
