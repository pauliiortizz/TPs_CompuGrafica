import glm

class Camera:
    def __init__(self, position, target, up, fov, aspect, near, far):
        self.position = glm.vec3(position)
        self.front = glm.normalize(glm.vec3(target) - self.position)
        self.up = glm.vec3(up)
        self.right = glm.normalize(glm.cross(self.front, self.up))

        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

        self.yaw = -90.0
        self.pitch = 0.0
        self.update_vectors()

    def get_perspective_matrix(self):
        return glm.perspective(glm.radians(self.fov), self.aspect, self.near, self.far)

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)

    def update_vectors(self):
        front = glm.vec3()
        front.x = glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        front.y = glm.sin(glm.radians(self.pitch))
        front.z = glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        self.front = glm.normalize(front)

        self.right = glm.normalize(glm.cross(self.front, glm.vec3(0.0, 1.0, 0.0)))
        self.up = glm.normalize(glm.cross(self.right, self.front))
