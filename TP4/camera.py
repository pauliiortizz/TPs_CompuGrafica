class Camera:
    def __init__(self):
        self.position = (0, 0, 0)
        self.orientation = (0, 0, 0)
        self.fov = 60  # Field of view in degrees

    def set_position(self, x, y, z):
        self.position = (x, y, z)

    def set_orientation(self, pitch, yaw, roll):
        self.orientation = (pitch, yaw, roll)

    def set_fov(self, fov):
        self.fov = fov