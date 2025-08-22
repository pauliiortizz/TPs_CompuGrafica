from PIL import Image

#funcion para crear un canvas
def new_canvas(width, height, backgroundColor = (2, 254, 230)):
    return [[backgroundColor for _ in range(width)] for _ in range(height)]


#funcion para pintar pixeles en el canvas
def set_pixel(canvas, x, y, color = (1,1,0)):
    height = len(canvas)
    width = len(canvas[0])
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = color


def save_png(filename, canvas):
    """Guarda la imagen en PNG usando Pillow.""" # Texto descriptivo para una función, esto es muy útil
    h = len(canvas)
    w = len(canvas[0])
    im = Image.new("RGB", (w, h))
    # Flatten de la lista de listas
    pixels_flat = [pixel for row in canvas for pixel in row] # recorre cada fila de img y dentro de cada fila recorre cada pixel para guardarlo en una sola lista.
    im.putdata(pixels_flat)
    im.save(f"{filename}.png", "PNG")