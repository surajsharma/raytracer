"""material / texture for shading"""

from color import Color

class Material:
    """material for shader has color and properties which make it react to light"""

    def __init__(self, color=Color.from_hex("#ffffff"), ambient=0.5, diffuse=1.0, specular=1.0):
        self.color=color
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
    
    def color_at(self, position):
        return self.color

        