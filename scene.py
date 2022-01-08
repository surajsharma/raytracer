"""accepts all ingredients for scene to render"""

class Scene:
    """has all the info needed for the engine"""

    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights =lights
        self.width = width
        self.height = height
        



