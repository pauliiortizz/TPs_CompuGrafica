import numpy as np
import glm

class Cube:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="Cube"):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)

        self.vertices = np.array([ 
            # posiciones        # colores 
            -1, -1, -1,  1, 0, 0, 
            1, -1, -1,  0, 1, 0, 
            1,  1, -1,  0, 0, 1, 
            -1,  1, -1,  1, 1, 0, 
            -1, -1,  1,  1, 0, 1, 
            1, -1,  1,  0, 1, 1, 
            1,  1,  1,  1, 1, 1, 
            -1,  1,  1,  0, 0, 0 
        ], dtype='f4')
        self.indices = np.array([ 
            0, 1, 2, 2, 3, 0,  # atrás 
            4, 5, 6, 6, 7, 4,  # frente 
            0, 4, 7, 7, 3, 0,  # izquierda 
            1, 5, 6, 6, 2, 1,  # derecha 
            3, 2, 6, 6, 7, 3,  # arriba 
            0, 1, 5, 5, 4, 0   # abajo 
        ], dtype='i4') 

    
    def get_model_matrix(self):
        model = glm.mat4(1.0)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1.0, 0.0, 0.0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0.0, 1.0, 0.0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0.0, 0.0, 1.0))
        model = glm.scale(model, self.scale)
        return model

    
