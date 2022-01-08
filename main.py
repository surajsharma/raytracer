#!/usr/bin/env python3
"""Ray Tracer"""

from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine

from light import Light
from material import Material

def main():
    """main function for ray tracer"""
    image_width = 320
    image_height = 200

    camera = Vector(0, 0, -1)
    objects = [
                    Sphere(Point(0, -0.35, 0), 0.15, Material(Color.from_hex("#ff0000"))),
                    Sphere(Point(0, 0.35, 0), 0.15, Material(Color.from_hex("#00ff00"))),
                    Sphere(Point(0, 0, 0.5), 0.23, Material(Color.from_hex("#0000ff")))
    ]

    lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#ffffff"))]
    scene = Scene(camera, objects, lights, image_width, image_height)

    engine = RenderEngine()
    image = engine.render(scene)

    with open("test.ppm", "w", encoding='UTF-8') as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()
