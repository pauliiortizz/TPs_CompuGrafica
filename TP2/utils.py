from PIL import Image

def new_canvas(width, height, backgroundColor=(0,0,0)):
    # aseguramos que sea tupla
    return [[tuple(backgroundColor) for _ in range(width)] for _ in range(height)]

def set_pixel(canvas, x, y, color=(255,255,255)): 
    height = len(canvas)
    width = len(canvas[0])
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = tuple(color)   # 🔑 forzamos a tupla

def save_png(canvas, filename):
    """Guarda la imagen en PNG usando Pillow."""
    h = len(canvas)
    w = len(canvas[0])
    im = Image.new("RGB", (w, h))
    # aplanamos forzando a tupla, por si acaso
    pixels_flat = [tuple(pixel) for row in canvas for pixel in row]
    im.putdata(pixels_flat)
    im.save(filename, "PNG")
