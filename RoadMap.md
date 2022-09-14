Pixly:

Backend: Python with Pillow Library
Frontend: Jinja...then React if time to spare


Pages:
-HomePage (displays all images with published as t)
-Search for photo
-Form for adding new photo
-Edit photo


Thing to Research:
-upload images
-retrieve metadata from photo(location, camera, etc) & store in AWS/DB
-store image file in AWS
-Users can search image data from the EXIF fields (you can learn about PostgreSQL full-text search)
-Edit photos with Pillow library
- upload photo to AWS - https://soshace.com/uploading-files-to-amazon-s3-with-flask-form-part1-uploading-small-files/

-type of data EXIF files gives back
-diff photos from diff devices have diff EXIF files


Database:
-columns for metadata
-columns for filters applied
-column for AWS URL
-column for published (boolean)
    if published f:
        be able to edit using pillow
        feature: find image not done editing (image id in url param)
    when user clicks done:
        published -> t

    columns:
        * filename (req)
        * published (req)
        * blackandwhite (opt)
        * sepia (opt)
        * downsized (opt)
        * border (opt)
        * metadata (holds JSON?)
        * tags 




User Perspective:
1. Arrive at homepage with edited photos
2. Click upload photo
3. Editing page with buttons that link pillow commands
4. Click publish
Feature: come back to unfinished photo, search for certain filters


Behind the Scenes:
1:
    - SQL call for all photos with published t 
        - use AWS stored URL as src for img

2:
    - add photo to AWS -> store AWS URL to DB
    - add photo to DB

3:

4: 

    
