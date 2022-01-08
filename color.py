"""Color class simply inherits vector"""

from vector import Vector


class Color(Vector):
    """inherit vector to store color as RGB"""

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        """convert hex to rgb"""
        v_x = int(hexcolor[1:3], 16)/255.0
        v_y = int(hexcolor[3:5], 16)/255.0
        v_z = int(hexcolor[5:7], 16)/255.0
        return cls(v_x, v_y, v_z)
