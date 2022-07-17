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


WIDTH = 960
HEIGHT = 540
RENDERED_IMG="twoballs.ppm"

CAMERA= Vector(0,-0.35, -1)

OBJECTS = [
    Sphere(Point(0,10000.5, 1), 10000.0, ChequeredMaterial(ambient=0.2, reflection=0.2)),
    Sphere(Point(0.75,-0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    Sphere(Point(-0.75,-0.1,2.25),0.6, Material(Color.from_hex("#FF90FF")))
]

LIGHTS = [
    Light(Point(1.5,-.5,-10), Color.from_hex("#000000")),
    Light(Point(-.5,-10.5,0), Color.from_hex("#000000"))
]
