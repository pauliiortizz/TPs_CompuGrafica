import numpy as np
import glm

class Cone:
    def __init__(self, radius=1.0, height=2.0, sectors=36,
                 position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="Cone"):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)

        vertices = []
        indices = []

        vertices.extend([0, height/2, 0, 1, 0, 0])  # rojo
        top_index = 0

        vertices.extend([0, -height/2, 0, 0, 1, 0])  # verde
        base_center_index = 1

        base_vertices = []
        for i in range(sectors):
            angle = 2 * np.pi * i / sectors
            x = radius * np.cos(angle)
            z = radius * np.sin(angle)
            y = -height/2
            r = (np.cos(angle)+1)/2
            g = (np.sin(angle)+1)/2
            b = 1.0
            vertices.extend([x, y, z, r, g, b])
            base_vertices.append(2 + i)

        for i in range(sectors):
            k1 = base_vertices[i]
            k2 = base_vertices[(i+1) % sectors]
            indices.extend([top_index, k1, k2])

        for i in range(sectors):
            k1 = base_vertices[i]
            k2 = base_vertices[(i+1) % sectors]
            indices.extend([base_center_index, k2, k1])

        self.vertices = np.array(vertices, dtype="f4")
        self.indices = np.array(indices, dtype="i4")

    def get_model_matrix(self):
        model = glm.mat4(1.0)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1.0, 0.0, 0.0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0.0, 1.0, 0.0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0.0, 0.0, 1.0))
        model = glm.scale(model, self.scale)
        return model
