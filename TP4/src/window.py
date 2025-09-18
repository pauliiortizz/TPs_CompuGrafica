import moderngl
import pyglet
from pyglet.window import key

class Window(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.ctx = moderngl.create_context()
        self.scene = None

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        self.set_exclusive_mouse(False)  
        self.last_x = width / 2
        self.last_y = height / 2
        self.first_mouse = True

    def set_scene(self, scene):
        self.scene = scene

    def on_draw(self):
        self.clear()
        self.ctx.clear()
        self.ctx.enable(moderngl.DEPTH_TEST)
        if self.scene:
            self.scene.render()

    def on_resize(self, width, height):
        if self.scene:
            self.scene.on_resize(width, height)


    def update(self, dt):
        if self.scene:
            cam = self.scene.camera
            speed = 0.2
            if self.keys[key.W]:
                cam.position += cam.front * speed
            if self.keys[key.S]:
                cam.position -= cam.front * speed
            if self.keys[key.A]:
                cam.position -= cam.right * speed
            if self.keys[key.D]:
                cam.position += cam.right * speed
            self.scene.view = cam.get_view_matrix()


    def on_mouse_motion(self, x, y, dx, dy):
        cam = self.scene.camera
        sensitivity = 0.1
        cam.yaw += dx * sensitivity
        cam.pitch += dy * sensitivity  

        if cam.pitch > 89.0: cam.pitch = 89.0
        if cam.pitch < -89.0: cam.pitch = -89.0

        cam.update_vectors()

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        pyglet.app.run()

    def save_screenshot(self, filename="scene.png"):
        buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        buffer.save(filename)
        print(f"✅ Screenshot guardado como {filename}")
        self.activate()


