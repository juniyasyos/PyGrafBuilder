import math
from OpenGL.GL import *

colors = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'White': (255, 255, 255),
    'Black': (0, 0, 0),
    'Aqua': (0, 255, 255),
    'Lime': (0, 255, 0),
    'Fuchsia': (255, 0, 255),
}

class ObjectManager:
    def __init__(self, objects=[]):
        self.objects = objects

    def get_objects(self):
        return self.objects

    def remove_objects(self, name="None"):
        if name == "All":
            self.objects.clear()
        else:
            self.objects = [obj for obj in self.objects if obj['type'] != name and obj['name'] != name]

    def set_objects(self, objects):
        self.objects = objects

    def create_rectangle(self, x, y, width, height, name="default", color=colors['White'], animation_type="pasif"):
        obj = {"name": name, "type": "rectangle", "x": x, "y": y, "width": width, "height": height,
               "animation_type": animation_type, "point": [(x, y), (x + width, y), (x + width, y + height), (x, y + height)], "color": color}
        self.objects.append(obj)

    def create_circle(self, x, y, radius, name="default", color=colors['White'], animation_type="pasif", opsi=1, k=6.276):
        poin = [(x + radius * math.cos(k - i * 3.1415926 / 180), y + radius * math.sin(k - i * 3.1415926 / 180)) for i in range(int(361 * opsi))]
        obj = {"name": name, "type": "circle", "x": x, "y": y, "radius": radius,
               "animation_type": animation_type, "point": poin, "color": color}
        self.objects.append(obj)

    def create_triangle(self, x, y, side_length, name="default", color=colors['White'], animation_type="pasif"):
        h = (side_length * math.sqrt(3)) / 2
        obj = {"name": name, "type": "triangle", "x": x, "y": y, "side_length": side_length,
               "animation_type": animation_type, "point": [(x, y), (x + side_length, y), (x + side_length / 2, y + h)], "color": color}
        self.objects.append(obj)

    def create_point(self, x, y, name="default", color=colors['White'], animation_type="pasif"):
        obj = {"name": name, "type": "point", "animation_type": animation_type, "x": x, "y": y, "color": color}
        self.objects.append(obj)

    def create_polygon(self, vertices: list, name="default", color=colors['White'], animation_type="pasif"):
        obj = {"name": name, "type": "polygon", "animation_type": animation_type, "point": vertices, "color": color}
        self.objects.append(obj)

    def create_line(self, x1=0, y1=0, x2=0, y2=0, length_line=0, degree=0, color=colors['White'], animation_type="pasif", lines=[], name="default"):
        if x2 != 0 and y2 != 0 and not lines:
            lines = [(x1, y1), (x2, y2)]
        else:
            x2 = x1 + length_line * math.cos(degree * math.pi / 180)
            y2 = y1 + length_line * math.sin(degree * math.pi / 180)
            lines = [(x1, y1)] + lines + [(x2, y2)]
        obj = {"name": name, "type": "line", "x1": x1, "y1": y1, "x2": x2, "y2": y2, 'point': lines,
               "animation_type": animation_type, "n_point": lines, "length_line": length_line, "degree": degree, "color": color}
        self.objects.append(obj)

    def draw_object(self):
        for obj in self.objects:
            getattr(self, f"draw_{obj['type']}")(obj)

    def draw_rectangle(self, obj):
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_QUADS)
        for p in obj['point']:
            glVertex2f(*p)
        glEnd()

    def draw_circle(self, obj):
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_TRIANGLE_FAN)
        for p in obj['point']:
            glVertex2f(*p)
        glEnd()

    def draw_triangle(self, obj):
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_TRIANGLES)
        for p in obj['point']:
            glVertex2f(*p)
        glEnd()

    def draw_point(self, obj):
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_POINTS)
        glVertex2f(obj["x"], obj["y"])
        glEnd()

    def draw_polygon(self, obj):
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_POLYGON)
        for p in obj["point"]:
            glVertex2f(*p)
        glEnd()

    def draw_line(self, obj):
        glColor3f(*obj['color'])
        glBegin(GL_LINES)
        for p1, p2 in zip(obj['point'], obj['point'][1:]):
            glVertex2f(*p1)
            glVertex2f(*p2)
        glEnd()
