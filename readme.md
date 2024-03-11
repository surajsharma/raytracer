# Raytracer

-   simple raytracer with multithreading written in Python.

[![asciicast](https://asciinema.org/a/NfxPm895hjRYTvJzflE00QeoA.svg)](https://asciinema.org/a/NfxPm895hjRYTvJzflE00QeoA)

#### How to use

1. create a scene file in `examples` or some other directory, name of the output file goes in here, like so

```
...
WIDTH = 960
HEIGHT = 540
RENDERED_IMG="twoballs.ppm"
...
```

2. invoke `main.py` with `python3` using the following arguments (example)

```
python3 main.py -scene examples.twoballs
```

3. the scene will be rendered in the file described within in the `examples` directory (in this case `twoballs.ppm`)asciinema rec
4. use a `ppm` viewer to see the rendered image
