from TP4.camera import Camera
from TP4.light import Light
from TP4.object import Object
class Scene:
    def __init__(self):
        self.objects = []
        self.camera = None
        self.lights = None
        self.initial_time = 0 
    
    def create_camera(self):
        self.camera = Camera()

    def create_lights(self):
        self.lights = Light()
    
    def add_object(self, object):
        self.objects.append(object)

    def render(self, context):
        for object in objects:
            object.render()


