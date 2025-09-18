from window import Window
from shader_program import ShaderProgram
from scene import Scene
from camera import Camera
from cube import Cube
from sphere import Sphere
from cone import Cone
import pyglet


window = Window(800, 600, "Basic Graphic Engine")
camera = Camera((0,0,10), (0,0,0), (0,1,0), 45, window.width/window.height, 0.1, 300.0)

shader = ShaderProgram(window.ctx,'../shaders/basic.vert','../shaders/basic.frag')
scene = Scene(window.ctx, camera)


cube1 = Cube((-2,0,0), (0,45,0), (0.5,0.5,0.5), name="Cube 1")
cube2 = Cube((2,0,0), (0,45,0), (0.5,0.5,0.5), name="Cube 2")
sphere = Sphere(radius=1.0, sectors=36, stacks=18, 
                position=(0,2,0), rotation=(0,0,0), scale=(0.5,0.5,0.5), name="Sphere 1")
cone = Cone(radius=1.0, height=2.0, sectors=36,
            position=(0,-2,0), rotation=(0,0,0), scale=(0.5,0.5,0.5), name="Cone 1")


scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader)
scene.add_object(cube2, shader)
scene.add_object(sphere, shader)
scene.add_object(cone, shader)

window.set_scene(scene)
def take_shot(dt):
    window.save_screenshot("mi_escena.png")

pyglet.clock.schedule_once(take_shot, 2.0)  # se guarda a los 2 segundos

window.run()

