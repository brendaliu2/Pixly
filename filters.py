from PIL import Image, ImageOps, ImagePalette
import io

def gray(image):
    '''Converts in-memory image to grayscale and returns image data for rendering.'''
    img = Image.open(image)
    gray_img = ImageOps.grayscale(img)
    in_mem_file = io.BytesIO()
    gray_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)
    return in_mem_file
    
def sepia(image):
    '''Converts in-memory image to sepia and returns image data for rendering.'''
    img = Image.open(image)
    palette = ImagePalette.sepia()
    sepia_img = img.convert('P')
    sepia_img.putpalette(palette.palette)

    in_mem_file = io.BytesIO()
    sepia_img.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)
    return in_mem_file

def random(image):
    '''Applies random color palette to in-memory image and returns image data for rendering.'''
    img = Image.open(image)
    palette = ImagePalette.random()
    sepia_img = img.convert('P')
    sepia_img.putpalette(palette.palette)

    in_mem_file = io.BytesIO()
    sepia_img.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)
    return in_mem_file

def border(image):
    '''Adds border to in-memory image and returns image data for rendering.'''
    img = Image.open(image)
    border_img = ImageOps.expand(img, 5, 'red')
    
    in_mem_file = io.BytesIO()
    border_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)
    return in_mem_file
    
def downsize(image):
    '''Scales down image for logo use and returns image data for rendering.'''
    img = Image.open(image)
    downsize_img = img.resize((100,100))
    
    in_mem_file = io.BytesIO()
    downsize_img.save(in_mem_file, format=img.format)
    in_mem_file.seek(0)
    return in_mem_file