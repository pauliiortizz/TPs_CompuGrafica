from window import Window
from scene import Scene

if __name__ == "__main__":
    window = Window(1280,720, "Graphic Engine")
    window.set_scene(Scene())
    window.run()
