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
        Image.write_ppm_header(
            img_fileobj, height=self.height, width=self.width)
        self.write_ppm_raw(img_fileobj)

    @staticmethod
    def write_ppm_header(img_fileobj, height=None, width=None):
        """Writes headers"""
        img_fileobj.write(f"P3 {width} {height}\n255\n")

    def write_ppm_raw(self, img_fileobj):
        """write a ppm file"""
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        for row in self.pixels:
            for color in row:
                img_fileobj.write(
                    f"{to_byte(color.v_x)} {to_byte(color.v_y)} {to_byte(color.v_z)} ")
                img_fileobj.write("\n")
