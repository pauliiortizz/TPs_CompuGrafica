import numpy as np
import glm

class Sphere:
    def __init__(self, radius=1.0, sectors=36, stacks=18, 
                 position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="Sphere"):
        self.name = name
        self.radius = radius
        self.sectors = sectors
        self.stacks = stacks
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)

        vertices = []
        indices = []

        # Generar vértices con colores (usamos coords esféricas)
        for i in range(stacks + 1):
            stack_angle = np.pi / 2 - i * np.pi / stacks  # de +90 a -90 grados
            xy = radius * np.cos(stack_angle)
            z = radius * np.sin(stack_angle)

            for j in range(sectors + 1):
                sector_angle = j * 2 * np.pi / sectors
                x = xy * np.cos(sector_angle)
                y = xy * np.sin(sector_angle)

                # Color basado en posición normalizada
                r = (x / radius + 1) / 2
                g = (y / radius + 1) / 2
                b = (z / radius + 1) / 2

                vertices.extend([x, y, z, r, g, b])

        # Generar índices para triángulos
        for i in range(stacks):
            k1 = i * (sectors + 1)
            k2 = k1 + sectors + 1
            for j in range(sectors):
                if i != 0:
                    indices.extend([k1 + j, k2 + j, k1 + j + 1])
                if i != (stacks - 1):
                    indices.extend([k1 + j + 1, k2 + j, k2 + j + 1])

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
