import numpy as np
import time
from OpenGL.GL import *
from OpenGL.GLUT import *

class Transform:
    def __init__(self, Objects=[]):
        self.Object = Objects

    def translate(self, dx: float, dy: float, name="default"):
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] in name or self.Object[obj]['type'] == name:
                for i in range(len(self.Object[obj]['point'])):
                    new_point.append((self.Object[obj]['point'][i][0] + dx,self.Object[obj]['point'][i][1] + dy))
                self.Object[obj]['point'] = new_point


    def scale(self, scale_factor,name="default"):
        "Hello"
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] in name or self.Object[obj]['type'] == name:
                print(self.Object[obj],['point'])
                self.Object[obj]['x'] *= scale_factor
                self.Object[obj]['y'] *= scale_factor
                for i in range(len(self.Object[obj]['point'])):
                    new_point.append((self.Object[obj]['point'][i][0] * scale_factor,self.Object[obj]['point'][i][1] * scale_factor))
                self.Object[obj]['point'] = new_point
                print(self.Object[obj],['point'])


    def rotate(self, angle_degrees, center_x=0.0, center_y=0.0, name="default"):
        """
        Rotate an object or shape by a specified angle (in degrees) around a specified center point.

        Args:
            angle_degrees (float): The rotation angle in degrees.
            center_x (float, optional): The x-coordinate of the center of rotation. Default is 0.0.
            center_y (float, optional): The y-coordinate of the center of rotation. Default is 0.0.
            name (str): The name of the object to be rotated. Default is "default".

        Returns:
            None
        """
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] == name or self.Object[obj]['type'] == name:
                angle_radians = np.radians(angle_degrees)
                for x, y in self.Object[obj]['point']:
                    # Translasi titik ke pusat rotasi
                    translated_x = x - center_x
                    translated_y = y - center_y

                    # Perhitungan rotasi
                    rotated_x = translated_x * np.cos(angle_radians) - translated_y * np.sin(angle_radians)
                    rotated_y = translated_x * np.sin(angle_radians) + translated_y * np.cos(angle_radians)

                    # Kembalikan ke posisi semula
                    final_x = rotated_x + center_x
                    final_y = rotated_y + center_y

                    new_point.append((final_x, final_y))

                self.Object[obj]['point'] = new_point
    
                



