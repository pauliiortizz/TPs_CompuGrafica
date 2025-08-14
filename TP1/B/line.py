def bresenham_line(x0, y0, x1, y1):
    points = []
    deltaX = abs(x1 - x0)
    deltaY = abs(y1 - y0)
    stepX = 1 if x0 < x1 else -1 # bool ? 1 : -1
    stepY = 1 if y0 < y1 else -1
    err = deltaX - deltaY

    while True:
        if x0 == x1 and y0 == y1:
            points.append((x0, y0))
            break
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -deltaY:
            err -= deltaY
            x0 += stepX
        if e2 < deltaX:
            err += deltaX
            y0 += stepY
        points.append((x0, y0))
    return points

def draw_line(x0, y0, x1, y1): #DDA Analizador de Direccion Digital
    points = []
    deltaX = x1 - x0
    deltaY = y1 - y0
    step = max(abs(deltaX), abs(deltaY))
    if step != 0:
        stepX = deltaX / step 
        stepY = deltaY / step 
        for i in range(step + 1):
            points.append((round(x0 + i * stepX), round(y0 + i * stepY)))
        return points
    
    # if deltaX == 0:


#funcion para crear un canvas
def new_canvas(width, height, backgroundColor = (0,255,0)):
    return [[backgroundColor for _ in range(width)] for _ in range(height)]


#funcion para pintar pixeles en el canvas
def set_pixel(canvas, x, y, color = (0,0,0)):
    height = len(canvas)
    width = len(canvas[0])
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = color

#funcion para mostrar el canvas en consola "renderizar"
def print_canvas(canvas):
    for row in canvas:
        print('|'.join(row))



def save_ppm_p3(filename, canvas):
    # encabezad que tipo p3 que tiene caracteres ascii, ancho, alto, rango de valores de colores
    # los colores
    height = len(canvas)
    width = len(canvas[0])
    with open(filename, 'w', encoding='ascii') as f:
        f.write(f'P3\n{width} {height}\n255\n') # encabezado
        # recorrer el canvas y escribir los colores
        for row in canvas:
            line = []
            for (r,g,b) in row:
                line.append(f"{r} {g} {b}")
            f.write(' '.join(line) + '\n')


# usando funciones
canvas = new_canvas(10, 10)

line = bresenham_line(0, 0, 7, 7)
for x, y in line:
    set_pixel(canvas, x, y)

#print_canvas(canvas)
save_ppm_p3('miPrimeraLinea.ppm', canvas)