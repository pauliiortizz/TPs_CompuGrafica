from utils import new_canvas, set_pixel, save_png

def draw_circle(centerX, centerY, radio):
    points = []
    x = 0 # al centro
    y = -radio # arriba
    while x < -y: # recorrer desde 0 hasta el radio
        points.append((centerX + x, centerY + y))
        x += 1
    return points

height = 256
width = 256
canvas = new_canvas(width, height)
circle = draw_circle(width//2, height//2, 20)
for x,y in circle:
    set_pixel(canvas, x,y)
save_png("circle", canvas)