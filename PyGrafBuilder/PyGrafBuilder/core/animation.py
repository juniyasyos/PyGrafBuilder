from OpenGL.GL import *
import math

class Transform:
    def __init__(self, objects=[]):
        self.objects = objects

    def translate(self, dx: float, dy: float, name="default"):
        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name or name in obj["group"]:
                obj["status"].append(["glTranslate",dx,dy,0])


    def scale(self, scale_factor, name="default"):
        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name or name in obj["group"]:
                    obj["status"].append(["glScale",scale_factor,scale_factor,0])

    def rotate(self, angle_degrees, center_x=0.0, center_y=0.0, name="default"):
        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name or name in obj["group"]:
                obj["status"].append(["glTranslate", center_x, center_y, 0])
                obj["status"].append(["glRotate", angle_degrees, 0, 0, 1])
                obj["status"].append(["glTranslate", -center_x, -center_y, 0])



class Animation:
    def __init__(self, transform):
        self.transform = transform

    def move_object_left(self, name, distance=10):
        self.transform.translate(-distance, 0, name)

    def move_object_right(self, name, distance=10):
        self.transform.translate(distance, 0, name)

    def move_object_up(self, name, distance=10):
        self.transform.translate(0, distance, name)

    def move_object_down(self, name, distance=10):
        self.transform.translate(0, -distance, name)

    def rotate_object_counterclockwise(self, name, angle_degrees=10, center_x=0.0, center_y=0.0):
        self.transform.rotate(-angle_degrees, center_x, center_y, name)
        
    def rotate_object_clockwise(self, name, angle_degrees=10, center_x=0.0, center_y=0.0):
        self.transform.rotate(angle_degrees, center_x, center_y, name)
