#!/usr/bin/env python3
"""Ray Tracer"""

import argparse
import importlib
import os

from scene import Scene
from engine import RenderEngine

def main():
    """main function for ray tracer"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-scene", help="Path to scene file")

    args = parser.parse_args()

    mod = importlib.import_module(args.scene)
    
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)

    engine = RenderEngine()
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    with open(mod.RENDERED_IMG, "w", encoding='UTF-8') as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()
