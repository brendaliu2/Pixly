# Pixly

Created with Flask and Jinja Template.
An photo editing app with users can upload a photo (save in AWS) and add different filters (greyscale, sepia, etc) to the photos.

## Run on your machine

```
git clone https://github.com/brendaliu2/Pixly.git
flask run -p 5001
```

## Must create .env file with following variables
* ACCESS_KEY
* SECRET_ACCESS_KEY
* BUCKET
* BASE_URL
* DATABASE_URL


## Future Features to Add

* Thorough Testing
* Make photos on homepage clickable for detail
* More filters
* Allow users to register and come back to unfinished photo
* Easy download edited photo to user computer at different resolutions

