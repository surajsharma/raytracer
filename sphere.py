from math import sqrt


class Sphere:
    """The only 3d shape implementedm, has radius, center, material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def normal(self, surface_point):
        """returns surface normal to the point on sphere's surface"""
        return (surface_point-self.center).normalize()

    def intersects(self, ray):
        """checks if ray intersects with sphere, returns distance or none"""
        sphere_to_ray = ray.origin - self.center

        _b = 2 * ray.direction.dot_product(sphere_to_ray)
        _c = sphere_to_ray.dot_product(
            sphere_to_ray) - self.radius * self.radius
        discriminant = _b*_b - 4*_c

        if discriminant >= 0:
            dist = (-_b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None
