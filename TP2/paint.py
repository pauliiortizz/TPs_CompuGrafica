import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import new_canvas, set_pixel, save_png
from bresenhamLine import bresenham_line
from middlePointCircle import middle_point_circle
from poligono import regular_polygon
import math

width = 400
height = 400 # Tamaño de canvas/ventana
color = (9, 150, 201) # Color de figuras

# 1) Crear el canvas lógico (array de píxeles) con WIDTH y HEIGHT, inicializado con fondo negro
canvas_data = new_canvas(width, height, (255,255,255))

# Tkinter setup
root = tk.Tk()
root.title("Mini Paint Casero")

# Imagen con Pillow para usar en Tkinter 
img = Image.new("RGB", (width, height), (255, 255, 255)) # Asigno un color de fondo de la ventana de dibujo
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

# Estado
mode = tk.StringVar(value="linea")
points = [] # Variable global de puntos

# Copia el canvas lógico a la imagen Pillow y la refresca en Tkinter, para poder mantener la lógica de nuestros algoritmos.
def redraw_canvas():
    global photo, img
    pixels = [pix for row in canvas_data for pix in row]
    img = Image.new("RGB", (width, height))
    img.putdata(pixels)
    photo = ImageTk.PhotoImage(img)
    label.configure(image=photo)
    label.image = photo

def on_click(event):
    global points
    x, y = event.x, event.y
    points.append((x,y))

    # --- Dibujar Línea ---
    if mode.get() == "linea" and len(points) == 2:
        x0,y0 = points[0]
        x1,y1 = points[1]
        linea = bresenham_line(x0, y0, x1, y1)
        for (px,py) in linea:
            set_pixel(canvas_data, px, py, color)
        redraw_canvas()
        points = []

    # --- Dibujar Rectángulo ---
    elif mode.get() == "rect" and len(points) == 2:
        x0, y0 = points[0]
        x1, y1 = points[1]
        # Lados
        for (a,b,c,d) in [(x0,y0,x1,y0), (x1,y0,x1,y1), (x1,y1,x0,y1), (x0,y1,x0,y0)]:
            lado = bresenham_line(a,b,c,d)
            for (px,py) in lado:
                set_pixel(canvas_data, px, py, color)
        redraw_canvas()
        points = []

    # --- Dibujar Círculo ---
    elif mode.get() == "circle" and len(points) == 2:
        xc,yc = points[0]
        x1,y1 = points[1]
        r = int(math.sqrt((x1-xc)**2 + (y1-yc)**2))
        circulo = middle_point_circle(xc,yc,r)
        for (px,py) in circulo:
            set_pixel(canvas_data, px, py, color)
        redraw_canvas()
        points = []

    # --- Dibujar Triángulo ---
    elif mode.get() == "triangulo" and len(points) == 3:
        for i in range(3):
            x0,y0 = points[i]
            x1,y1 = points[(i+1)%3]
            lado = bresenham_line(x0,y0,x1,y1)
            for (px,py) in lado:
                set_pixel(canvas_data, px, py, color)
        redraw_canvas()
        points = []

    elif mode.get() == "poligono" and len(points) == 2:
        xc, yc = points[0]
        x1, y1 = points[1]
        r = int(math.sqrt((x1-xc)**2 + (y1-yc)**2))
        n = 6  # por ejemplo hexágono fijo, o podés pedirlo con un input
        poligono = regular_polygon(xc, yc, r, n)
        for (px, py) in poligono:
            set_pixel(canvas_data, px, py, color)
        redraw_canvas()
        points = []


def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if filename:
        save_png(canvas_data, filename)

# Botones de modo
frame = tk.Frame(root)
frame.pack()
for m in [("Linea","linea"), ("Rectangulo","rect"), ("Circulo","circle"), ("Triangulo","triangulo"), ("Poligono", "poligono")]:
    b = tk.Radiobutton(frame, text=m[0], variable=mode, value=m[1])
    b.pack(side="left")

# Botón Guardar
save_btn = tk.Button(root, text="Guardar PNG", command=save_image)
save_btn.pack()

# Bind click
label.bind("<Button-1>", on_click)

root.mainloop()
