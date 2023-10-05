from OpenGL.GL import *
import math

class Transform:
    def __init__(self, objects=[]):
        self.objects = objects

    def translate(self, dx: float, dy: float, name="default"):
        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name:
                for i in range(len(obj['point'])):
                    x, y = obj['point'][i]
                    x += dx
                    y += dy
                    obj['point'][i] = (x, y)

    def scale(self, scale_factor, name="default"):
        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name:
                for i in range(len(obj['point'])):
                    x, y = obj['point'][i]
                    x *= scale_factor
                    y *= scale_factor
                    obj['point'][i] = (x, y)

    def rotate(self, angle_degrees, center_x=0.0, center_y=0.0, name="default"):
        angle_radians = math.radians(angle_degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)

        for obj in self.objects:
            if obj['name'] == name or obj['type'] == name:
                for i in range(len(obj['point'])):
                    x, y = obj['point'][i]
                    translated_x = x - center_x
                    translated_y = y - center_y

                    rotated_x = translated_x * cos_theta - translated_y * sin_theta
                    rotated_y = translated_x * sin_theta + translated_y * cos_theta

                    final_x = rotated_x + center_x
                    final_y = rotated_y + center_y

                    obj['point'][i] = (final_x, final_y)


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
