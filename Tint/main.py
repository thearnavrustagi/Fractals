from PIL import Image
from PIL import ImageOps

def tint_image(src, color="#FFFFFF"):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    #result = ImageOps.colorize(gray,'#E1FF17',color) 
    result = ImageOps.colorize(gray,'#000000','#debb9c') 
    result.putalpha(alpha)
    return result

img = Image.open("penguins.png").transpose(Image.FLIP_LEFT_RIGHT)
tinted = tint_image(img, "#DEBB9C")
tinted.show()
tinted.save('output.png')
