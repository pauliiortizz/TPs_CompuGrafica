import pyglet
import moderngl

class Window(pyglet.window.Window):
    def __init__(self, width,height,title):
        super().__init__(width, height, title, resizable=True)
        self.context = moderngl.create_context()
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene
    
    def on_draw(self):
        self.clear()
        self.context.clear(0.1, 0.1, 0.1)
        if self.scene:
            self.scene.render(self.context)

    def run(self):
        pyglet.app.run()