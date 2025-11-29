import os

ASCII = " .:-=+*#%@"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class AsciiDisplay:
    def draw(self, fb):
        clear()
        for row in fb.pixels:
            line = "".join(ASCII[int(v * (len(ASCII) - 1))] for v in row)
            print(line)
