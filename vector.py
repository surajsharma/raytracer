import math


class Vector:
    """multipurpose 3d vector"""

    def __init__(self, v_x=0.0, v_y=0.0, v_z=0.0):
        """constructor for vector"""
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def __str__(self):
        """stringify a vector"""
        return f"({self.v_x},{self.v_y},{self.v_z})"

    def magnitude(self):
        """magnitude of vector"""
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        """normalized vector"""
        return self / self.magnitude()

    def __add__(self, other):
        """add vector to other vector"""
        return Vector(self.v_x + other.v_x, self.v_y + other.v_y, self.v_z + other.v_z)

    def __sub__(self, other):
        """deduct vector from other vector"""
        return Vector(self.v_x - other.v_x, self.v_y - other.v_y, self.v_z - other.v_z)

    def dot_product(self, other):
        """dot product is vector multiplication"""
        return self.v_x * other.v_x + self.v_y * other.v_y + self.v_z * other.v_z

    def __mul__(self, other):
        """multiply vector with scalar"""
        assert not isinstance(other, Vector)  # ensure other is not vector
        return Vector(self.v_x * other, self.v_y * other, self.v_z * other)

    def __rmul__(self, other):
        """multiplication by other dunder"""
        return self.__mul__(other)

    def __truediv__(self, other):
        """divide vector with scalar"""
        assert not isinstance(other, Vector)  # ensure other is not scalar
        return Vector(self.v_x / other, self.v_y / other, self.v_z / other)
