from camera import Camera
from light import Light
from object import Object

class Scene:
    def __init__(self):
        self.objects = []
        self.camera = None
        self.light = None
        self.initial_time = 0 
    
    def create_camera(self):
        self.camera = Camera()

    def create_lights(self):
        self.lights = Light()
    
    def add_object(self, object):
        self.objects.append(object)

    def render(self, context):
        for object in self.objects:
            object.render()


