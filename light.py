"""light source for shader"""

from color import Color


class Light:
    """point light with color"""

    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
