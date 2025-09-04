import pyglet  # Librería que crea la ventana y el loop de eventos (inputs, redraws)
import moderngl  # API de OpenGL que simplifica manejo de contexto y buffers
import numpy as np  # Para arrays numéricos (matrices, buffers de vértices)
from pathlib import Path
import time

class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "TP3 - Ortiz")
        self.ctx = moderngl.create_context()
        self.start_time = time.time()
        self.mouse_x, self.mouse_y = 0.0, 0.0
        self.zoom = 1.0  # 👈 Zoom inicial (1.0 = normal)

        shader_dir = Path(__file__).parent / "shader"
        with open(shader_dir / "vertex.glsl") as f:
            vertex_shader_src = f.read()
        with open(shader_dir / "fragment.glsl") as f:
            fragment_shader_src = f.read()

        self.prog = self.ctx.program(
            vertex_shader=vertex_shader_src,
            fragment_shader=fragment_shader_src
        )

        quad = np.array([
            -1.0, -1.0,
             1.0, -1.0,
            -1.0,  1.0,
             1.0,  1.0
        ], dtype="f4")

        vbo = self.ctx.buffer(quad.tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, vbo, "in_pos")

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # scroll_y > 0 → acercar, scroll_y < 0 → alejar
        self.zoom *= 1.0 + scroll_y * 0.1
        self.zoom = max(0.2, min(self.zoom, 5.0))  # 👈 limitar zoom (0.2x a 5x)

    def on_draw(self):
        self.clear()
        self.ctx.clear(0.0, 0.0, 0.0)

        self.prog["iTime"].value = time.time() - self.start_time
        self.prog["iResolution"].value = (self.width, self.height)
        self.prog["iMouse"].value = (self.mouse_x, self.mouse_y, 0.0, 0.0)
        self.prog["iZoom"].value = self.zoom  # 👈 pasamos el zoom

        self.vao.render(moderngl.TRIANGLE_STRIP)



if __name__ == "__main__":
    Window()
    pyglet.app.run()

