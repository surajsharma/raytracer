#!/usr/bin/env python3
"""Ray Tracer"""

import argparse
import importlib
import os

from scene import Scene
from engine import RenderEngine

from multiprocessing import cpu_count

def main():
    """main function for ray tracer"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-scene", help="Path to scene file")
    parser.add_argument("-p", "--processes" , action="store", type=int, dest="processes", default=0, help="Number of processes (0=auto)")

    args = parser.parse_args()

    if args.processes == 0:
        process_count = cpu_count()
    else:
        process_count = args.processes

    mod = importlib.import_module(args.scene)
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    with open(mod.RENDERED_IMG, "w", encoding='UTF-8') as img_fileobj:
        engine.render_multiprocess(scene, process_count, img_fileobj)

if __name__ == "__main__":
    main()
