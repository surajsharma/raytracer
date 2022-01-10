"""Example twoballs"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.


from color import Color

from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene

from light import Light
from material import Material

import math

from random import randint
from material import ChequeredMaterial


WIDTH = 320
HEIGHT = 200
RENDERED_IMG="2balls.ppm"
CAMERA= Vector(0,-0.35, -1)

OBJECTS = [
    Sphere(Point(0,10000.5, 1), 10000.0, ChequeredMaterial(ambient=0.2, reflection=0.2)),
    Sphere(Point(0.75,-0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    Sphere(Point(-0.75,-0.1,2.25),0.6, Material(Color.from_hex("#803980")))
]
LIGHTS = [
    Light(Point(1.5,-.5,-10), Color.from_hex("#FFFFFF")),
    Light(Point(-.5,-10.5,0), Color.from_hex("#E6E6E6"))
]

# camera = Vector(0, 0, -1)

# radius = 0.2

# objects = [
#                 Sphere(Point(0, 0, 0), radius, Material(Color.from_hex("#ff7701")))
# ]

# slices = 32

# for i in range(slices):
#     angle = math.radians(360.0/slices * i * randint(-2,2))
#     for j in range(3):
#         #polar coords to cartesian
#         stem_radius = 0.008
#         x = (radius+stem_radius*j)*math.sin(angle)
#         y = (radius+stem_radius*j)*math.cos(angle)
#         objects.append(Sphere(Point(x,y,0), stem_radius, Material(Color.from_hex("#d47721"))))

#         blob_radius = 0.01
#         x = (radius+stem_radius*j*blob_radius)*math.sin(angle)
#         y = (radius+stem_radius*j*blob_radius)*math.cos(angle)
#         objects.append(Sphere(Point(x,y,0), blob_radius, Material(Color.from_hex("#febd14"))))


# lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#ff4900"))]
# scene = Scene(camera, objects, lights, image_width, image_height)

# engine = RenderEngine()
# image = engine.render(scene)

