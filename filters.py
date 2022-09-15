from PIL import Image, ImageOps, ImagePalette
import io

# Make image black/white
def gray(image):
    img = Image.open(image)
    gray_img = ImageOps.grayscale(img)
    in_mem_file = io.BytesIO()
    gray_img.save(in_mem_file, format=img.format)
    # in_mem_file.seek(0)
    return in_mem_file
    

# Make image sepia
# FIXME: DOES NOT WORK RIGHT WITH PNGS RIGHT NOW (oh well?)
def sepia(image):
    img = Image.open(image)
    palette = ImagePalette.sepia()
    sepia_img = img.convert('P')
    sepia_img.putpalette(palette.palette)

    in_mem_file = io.BytesIO()
    sepia_img.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)
    return in_mem_file

# Make image random color palette
def random(image):
    img = Image.open(image)
    palette = ImagePalette.random()
    sepia_img = img.convert('P')
    sepia_img.putpalette(palette.palette)

    in_mem_file = io.BytesIO()
    sepia_img.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)
    return in_mem_file

# Add Image Border
def border(image):
    img = Image.open(image)
    border_img = ImageOps.expand(img, 5)
    
    in_mem_file = io.BytesIO()
    border_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)
    return in_mem_file
    

# Change Image Size
def resize(image):
    img = Image.open(image)
    resize_img = img.resize((20,20))
    
    in_mem_file = io.BytesIO()
    resize_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)
    return in_mem_file