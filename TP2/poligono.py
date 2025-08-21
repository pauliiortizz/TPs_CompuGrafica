import math
from bresenhamLine import bresenham_line

def regular_polygon(xc, yc, r, n):
    points = []
    vertices = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = int(xc + r * math.cos(angle))
        y = int(yc + r * math.sin(angle))
        vertices.append((x, y))
    # Dibujar lados con Bresenham
    for i in range(n):
        x0,y0 = vertices[i]
        x1,y1 = vertices[(i+1)%n]
        points.extend(bresenham_line(x0,y0,x1,y1))
    return points