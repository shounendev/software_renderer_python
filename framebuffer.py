class Framebuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0.0 for _ in range(width)] for _ in range(height)]

    def clear(self, value=0.0):
        for y in range(self.height):
            for x in range(self.width):
                self.pixels[y][x] = value

    def set_pixel(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = value
