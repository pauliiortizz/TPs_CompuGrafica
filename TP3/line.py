def bresenham_line(x0, y0, x1, y1):
    points = []
    deltaX = abs(x1 - x0)
    deltaY = abs(y1 - y0)
    stepX = 1 if x0 < x1 else -1 # bool ? 1 : -1
    stepY = 1 if y0 < y1 else -1
    err = deltaX - deltaY

    while x0 != x1 or y0 != y1:
        points.append((x0,y0))
        e2 = 2 * err
        if e2 > -deltaY: #corrige en X
            err -= deltaY
            x0 += stepX
        if e2 < deltaX: #corrige en y
            err += deltaX
            y0 += stepY
    return points

def draw_line(x0, y0, x1, y1): # DDA Analizador de Direccion Digital
    # retorno esperado: return [(x,y), (x,y)]
    points = []
    deltaX = x1 - x0
    deltaY = y1 - y0
    step = max(abs(deltaX), abs(deltaY))
    if step != 0:
        stepX = deltaX / step # max deltaX
        stepY = deltaY / step # si uno es 1 o -1, el otro tiene el valor de la pendiente
        for i in range(step + 1):
            points.append((round(x0 + i * stepX), round(y0 + i * stepY)))
        return points

# Funcion para crear un canvas.
def new_canvas(width, height, backgroundColor = (0,0,0)):
    return [[backgroundColor for _ in range(width)] for _ in range(height)]        

# Funcion para pintar "pixeles" en el canvas.
def set_pixel(canvas, x, y, color=(255,255,255)):
    """color debe ser (r,g,b)"""
    h = len(canvas)
    w = len(canvas[0])
    if 0 <= x < w and 0 <= y < h:
        # fuerza a que cada componente sea int (por si viene como float)
        r, g, b = map(int, color)
        canvas[y][x] = (r, g, b)

# Funcion para mostrar el canvas en consola "renderizar".
def print_canvas(canvas):
    for row in canvas:
        print('|'.join(row))

def save_ppm_p3(filename, canvas):
    # Encabezado, que tipo p3 que tiene caracteres ascii, ancho, alto, rango de valores de colores
    # los colores
    height = len(canvas)
    width = len(canvas[0])
    with open(filename, "w", encoding = "ascii") as f:
        f.write(f"P3\n{width} {height}\n255\n") #encabezado
        #es escribir (pasar a string) linea por linea los colores.
        for row in canvas:
            line = []
            for (r,g,b) in row:
                line.append(f"{r} {g} {b}") #to string
            f.write(' '.join(line) + "\n")

#usando funciones jeje
canvas = new_canvas(64, 64)   # fondo negro por default

# --- Definir colores ---
celeste = (135, 206, 235)
blanco  = (255, 255, 255)

# --- Definir las líneas de la estrella (ejemplo 5 puntas) ---
lineas = [
    ((32, 0),  (12, 63), celeste),
    ((12, 63), (63, 24), blanco),
    ((63, 24), (1, 24),  celeste),
    ((1, 24),  (52, 63), blanco),
    ((52, 63), (32, 0),  celeste),
]

# --- Dibujar las líneas ---
for (p0, p1, color) in lineas:
    x0, y0 = p0
    x1, y1 = p1
    for x, y in bresenham_line(x0, y0, x1, y1):
        set_pixel(canvas, x, y, color)

# --- Guardar a archivo ---
save_ppm_p3("miPrimeraLinea.ppm", canvas)