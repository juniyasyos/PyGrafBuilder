import numpy as np

class Transform:
    def __init__(self, Objects=[]):
        """
        Initializes a new instance of the Transform class.

        The Transform class provides methods to perform various transformations (translation, scaling, rotation)
        on objects or shapes in a 2D OpenGL scene.

        Args:
            Objects (list of dict, optional): A list of objects to be manipulated. Default is an empty list.

        Returns:
            None
        """
        self.Object = Objects

    def translate(self, dx: float, dy: float, name="default"):
        """
        Translate an object or shape by a specified displacement.

        Args:
            dx (float): The displacement along the x-axis.
            dy (float): The displacement along the y-axis.
            name (str, optional): The name or type of object to be translated. Default is "default" (all objects).

        Returns:
            None
        """
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] in name or self.Object[obj]['type'] == name:
                for i in range(len(self.Object[obj]['point'])):
                    new_point.append((self.Object[obj]['point'][i][0] + dx,self.Object[obj]['point'][i][1] + dy))
                self.Object[obj]['point'] = new_point


    def scale(self, scale_factor,name="default"):
        """
        Scale an object or shape by a specified scaling factor.

        Args:
            scale_factor (float): The scaling factor.

        Returns:
            None
        """
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] in name or self.Object[obj]['type'] == name:
                for i in range(len(self.Object[obj]['point'])):
                    new_point.append((self.Object[obj]['point'][i][0] * scale_factor,self.Object[obj]['point'][i][1] * scale_factor))
                self.Object[obj]['point'] = new_point

    def rotate(self, angle_degrees, name="default"):
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
        pointCenter = 0
        for obj in range(len(self.Object)):
            new_point = []
            if self.Object[obj]['name'] == name or self.Object[obj]['type'] == name:
                angle_radians = np.radians(angle_degrees)
                x_total = 0
                y_total = 0
                for x,y in range(len(self.Object[obj]['point'])):
                    x_total += x                    
                    y_total += y           
                mid = (x_total/len(self.Object[obj]['point']),y_total/len(self.Object[obj]['point']))         
                
                self.Object[obj]['point'] = new_point
        pass
                


                
    def apply_transf(self):
        """
        Returns the list of objects after applying transformations.

        Args:
            None

        Returns:
            list of dict: The list of objects after applying transformations.
        """
        return self.Object
    
