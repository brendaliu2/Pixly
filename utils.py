import uuid
import json

# PILLOW IMPORTS
from PIL import Image, ExifTags, TiffImagePlugin
from PIL import Image

# GLOBAL CONSTANTS
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

from filters import *

##################### UTILITY FUNCTIONS ##################### 

def allowed_file(filename):
    '''
    Checks that uploaded file has one of allowed file extensions. 
    Returns a boolean.
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(filename):
    '''
    Generates random unique filename using UUID and reattaches file extension. 
    Returns new filename.
    '''
    file_uuid = str(uuid.uuid4())
    file_extension = filename.rsplit('.', 1)[1].lower()
    return f"{file_uuid}.{file_extension}"
    
def cast(v):
    '''
    Helper function to standarize exif dict entries for JSON compatibility
    '''
    if isinstance(v, TiffImagePlugin.IFDRational):
        return float(v)
    elif isinstance(v, tuple):
        return tuple(cast(t) for t in v)
    elif isinstance(v, bytes):
        return v.decode(errors="replace")
    elif isinstance(v, dict):
        for kk, vv in v.items():
            v[kk] = cast(vv)
        return v
    else: return v
    
def get_exif_data(image):
    '''
    Access EXIF data from image and return dictionary of key/value pairs.
    '''
    img = Image.open(image)
    img_exif = img.getexif()
    
    file_exif_dict = {}
    exif_dict = {}
       
    if img_exif is None:
        return None
    else:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                val = cast(val)
                exif_dict[ExifTags.TAGS[key]]=val
    
    exif_str = json.dumps(exif_dict)
    
    in_mem_file = io.BytesIO()
    img.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)
    
    file_exif_dict['file'] = in_mem_file
    file_exif_dict['exif'] = exif_str
    return file_exif_dict


def set_filter(file, filter):
    '''
    Filter a provided file based on requested filter.
    Returns filtered image or, if no filter is requested/no matching filter found,
    returns original file for processing.
    '''
    if filter == 'gray':
            img = gray(file)
    elif filter == 'sepia':
            img = sepia(file)
    elif filter == 'border':
            img = border(file)
    elif filter == 'downsize':
            img = downsize(file)
    elif filter == 'random':
            img = random(file)
    else: 
            return file
        
    return img