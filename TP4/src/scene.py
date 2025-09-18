import glm
from graphics import Graphics

class Scene:
    def __init__(self, ctx, camera):
        self.ctx = ctx
        self.camera = camera
        self.objects = []
        self.graphics = {}
        self.model = glm.mat4(1.0)
        self.view = camera.get_view_matrix()
        self.projection = camera.get_perspective_matrix()

    def add_object(self, obj, shader_program=None):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)
    
    def render(self):
        for obj in self.objects:
            model = obj.get_model_matrix()
            mvp = self.projection * self.view * model

            self.graphics[obj.name].set_uniform("Mvp", mvp)

            self.graphics[obj.name].vao.render()


    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.aspect = width / height
        self.projection = self.camera.get_perspective_matrix()
