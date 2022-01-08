"""Image class for rayt racer"""


class Image:
    """image class"""

    def __init__(self, i_w, i_h):
        self.width = i_w
        self.height = i_h
        self.pixels = [[None for _ in range(i_w)] for _ in range(i_h)]

    def set_pixel(self, p_x, p_y, col):
        """setting a pixel"""
        self.pixels[p_y][p_x] = col

    def write_ppm(self, img_file):
        """write a ppm file"""
        def to_byte(_c):
            return round(max(min(_c * 255, 255), 0))

        img_file.write(f"P3 {self.width} {self.height}\n255\n")

        for row in self.pixels:
            for color in row:
                img_file.write(
                    f"{to_byte(color.v_x)} {to_byte(color.v_y)} {to_byte(color.v_z)} ")
                img_file.write("\n")
