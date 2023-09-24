import math
from OpenGL.GL import *
import json

colors = {
        'Red': (255, 0, 0),
        'Green': (0, 255, 0),
        'Blue': (0, 0, 255),
        'Yellow': (255, 255, 0),
        'Cyan': (0, 255, 255),
        'Magenta': (255, 0, 255),
        'White': (255, 255, 255),
        'Black': (0, 0, 0),
        'Gray': (128, 128, 128),
        'Aqua': (0, 255, 255),
        'Lime': (0, 255, 0),
        'Navy': (0, 0, 128),
        'Fuchsia': (255, 0, 255),
        'Olive': (128, 128, 0),
        'Teal': (0, 128, 128),
        'Maroon': (128, 0, 0),
    }

class ObjectManager:
    """
    Manages objects in the OpenGL scene.
    """
    def __init__(self,objects=[]):
        self.objects = objects
        self.setting_animation = SettingAnimation(self.objects)

    def get_Objects(self):
        def load_json(filename):
            """ Membaca data dari file JSON. """
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                return data
            except FileNotFoundError:
                print(f"File {filename} tidak ditemukan.")
                return []
            except Exception as e:
                print(f"Terjadi kesalahan saat membaca file {filename}: {str(e)}")
                return []
        file = ["D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/pasif_objek.json","D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/aktif_objek.json","D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/entahlah_objek.json"]
        data = []
        for i in file:
            for j in load_json(i):
                data.append(j)
                
        self.objects = data
        return self.objects

    def remove_objects(self, name="None"):
        """
        Remove objects from the Object Manager.

        Args:
            name (str, optional): The name or type of objects to remove. Default is "None" which does nothing.
                You can use "All" to remove all objects, or specify the type of objects to remove
                (e.g., "circle", "rectangle", "triangle", "line", "polygon", "point").

        Example:
            # Remove all objects
            object_manager.remove_objects("All")

            # Remove all circle objects
            object_manager.remove_objects("circle")

            # Remove all objects of a specific name (user-defined)
            object_manager.remove_objects("my_object")

            # Do nothing (default behavior)
            object_manager.remove_objects()
        """
        if name == "All":
            self.objects.clear()
        else:
            # Create a list to store objects to be removed
            to_remove = []

            for obj in self.objects:
                if name == "None" or obj['type'] == name or obj['name'] == name:
                    to_remove.append(obj)

            # Remove objects from the to_remove list
            for obj in to_remove:
                self.objects.remove(obj)

    def set_objects(self,objects):
        self.objects=objects

    def create_rectangle(self, x, y, width, height,name="default", color=colors['White'],animation_type="pasif"):
        """
        Create a rectangle object.

        Args:
            x (float): X-coordinate of the rectangle's origin.
            y (float): Y-coordinate of the rectangle's origin.
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
            color (tuple, optional): Color of the rectangle in RGB format. Default is white (1.0, 1.0, 1.0).
        """
        obj = {
            "name": name,
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "animation_type":animation_type,
            "point":[(x, y),(x + width, y),(x + width, y + height),(x, y + height)],
            "color": color
        }
        self.objects.append(obj)
    
    def create_circle(self, x, y, radius, name="default", color=colors['White'],animation_type="pasif",opsi=1,k=6.276):
        """
        Create a circle object.

        Args:
            x (float): X-coordinate of the circle's center.
            y (float): Y-coordinate of the circle's center.
            radius (float): Radius of the circle.
            color (tuple, optional): Color of the circle in RGB format. Default is white (1.0, 1.0, 1.0).
        """
        poin = []
        dg = int(361*opsi)
        for i in range(dg):
            angle = k-i * 3.1415926 / 180
            poin.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
        obj = {
            "name": name,
            "type": "circle",
            "x": x,
            "y": y,
            "radius": radius,
            "animation_type":animation_type,
            "point":poin,
            "color": color
        }
        self.objects.append(obj)

    def create_triangle(self, x, y, side_length, name="default",color=colors['White'],animation_type="pasif"):
        """
        Create a triangle object.

        Args:
            x (float): X-coordinate of the triangle's origin.
            y (float): Y-coordinate of the triangle's origin.
            side_length (float): Length of each side of the equilateral triangle.
            color (tuple, optional): Color of the triangle in RGB format. Default is white (1.0, 1.0, 1.0).
        """

        obj = {
            "name": name,
            "type": "triangle",
            "x": x,
            "y": y,
            "side_length": side_length,
            "animation_type":animation_type,
            "point":[(x, y),(x + side_length, y),(x + side_length / 2, y + (side_length * math.sqrt(3)) / 2)],
            "color": color
        }
        self.objects.append(obj)

    def create_point(self, x, y, name="default",color=colors['White'],animation_type="pasif"):
        """
        Create a point object.

        Args:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the point.
            color (tuple, optional): Color of the point in RGB format. Default is white (1.0, 1.0, 1.0).
        """
        obj = {
            "name": name,
            "type": "point",
            "animation_type":animation_type,
            "x": x,
            "y": y,
            "color": color
        }
        self.objects.append(obj)

    def create_polygon(self, vertices:list, name="default", color=colors['White'],animation_type="pasif"):
        """
        Create a polygon object.

        Args:
            vertices (list of tuple): List of vertex positions in the format [(x1, y1), (x2, y2), ...].
            color (tuple, optional): Color of the polygon in RGB format. Default is white (1.0, 1.0, 1.0).
        """
        obj = {
            "name": name,
            "type": "polygon",
            "animation_type":animation_type,
            "point": vertices,
            "color": color
        }
        self.objects.append(obj)

    def create_line(self, x1=0, y1=0, x2=0, y2=0, length_line=0, degree=0, color=colors['White'],animation_type="pasif",lines=[],name="default",):
        """
        Create a line object.

        Args:
            x1 (float): X-coordinate of the starting point of the line.
            y1 (float): Y-coordinate of the starting point of the line.
            x2 (float): X-coordinate of the ending point of the line.
            y2 (float): Y-coordinate of the ending point of the line.
            length_line (float): Length of the line (optional).
            degree (float): Rotation angle in degrees (optional).
            color (tuple, optional): Color of the line in RGB format. Default is white (1.0, 1.0, 1.0).
        """
        point = []
        if x2 != 0 and y2 != 0 and lines==[]:
            point.append((x1,y1))
            point.append((x2,y2))
        else:
            x2 = x1 + length_line * math.cos(degree * math.pi / 180.0)
            y2 = y1 + length_line * math.sin(degree * math.pi / 180.0)
            point.append((x1,y1))
            for i in lines:
                point.append(i)
            point.append((x2,y2))
        obj = {
            "name": name,
            "type": "line",
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            'point':point,
            "animation_type":animation_type,
            "n_point":lines,
            "length_line": length_line,
            "degree": degree,
            "color": color
        }
        self.objects.append(obj)

    def draw_object(self):
        """
        Draw the specified objects on the screen.
        """
        for obj in self.objects:
            if obj["type"] == "rectangle":
                self.draw_rectangle(obj)
            elif obj["type"] == "circle":
                self.draw_circle(obj)
            elif obj["type"] == "triangle":
                self.draw_triangle(obj)
            elif obj["type"] == "point":
                self.draw_point(obj)
            elif obj["type"] == "line":
                self.draw_line(obj)
            elif obj["type"] == "polygon":
                self.draw_polygon(obj)
                
    def draw_rectangle(self, obj):
        """
        Draw a rectangle object.
        """
        color = obj["color"]

        glColor3f(*color)
        glBegin(GL_QUADS)
        for i in range(len(obj['point'])):
            glVertex2f(*obj['point'][i])
        glEnd()

    def draw_circle(self, obj):
        """
        Draw a circle object.
        """
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_TRIANGLE_FAN)
        for i in range(len(obj['point'])):
            glVertex2f(*obj['point'][i])
        glEnd()

    def draw_triangle(self, obj):
        """
        Draw a triangle object.
        """
        color = obj["color"]
        glColor3f(*color)
        glBegin(GL_TRIANGLES)
        for i in range(len(obj['point'])):
            glVertex2f(*obj['point'][i])
        glEnd()

    def draw_point(self, obj):
        """
        Draw a point object.
        """
        x = obj["x"]
        y = obj["y"]
        color = obj["color"]

        glColor3f(*color)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    def draw_polygon(self, obj):
        """
        Draw a polygon object.
        """
        vertices = obj["point"]
        color = obj["color"]

        glColor3f(*color)
        glBegin(GL_POLYGON)
        for vertex in vertices:
            glVertex2f(*vertex)
        glEnd()

    def draw_line(self, obj):
        """
        Draw a line object.
        """
        glColor3f(*obj['color'])
        glBegin(GL_LINES)
        for i in range(len(obj['point'])):
            if i+1 != len(obj['point']):
                glVertex2f(*obj['point'][i])
                glVertex2f(*obj['point'][i+1])
        glEnd()


class SettingAnimation:
    """ Kelas untuk mengatur animasi objek. """
    
    def __init__(self, objects):
        self.objects = objects

    def setAnimation(self, name: list or str, animation_type: str):
        """ Mengatur tipe animasi objek berdasarkan nama objek. """
        for obj in self.objects:
            if obj['name'] in name:
                obj["animation_type"] = animation_type
    

    def saveObjectGraf(self):
        def saveFile(objects, filename):
            """ Menyimpan objek ke dalam file JSON. """
            try:
                with open(filename, "a") as file:
                    json.dump(objects, file, indent=4)

                print(f"Objek berhasil disimpan ke dalam file: {filename}")
            except Exception as e:
                print(f"Terjadi kesalahan saat menyimpan objek: {str(e)}")
        
        pasif_obj = []
        aktif_obj = []
        tau_obj = []
        for obj in self.objects:
            if obj["animation_type"] == "pasif":
                pasif_obj.append(obj)
            elif obj["animation_type"] == "aktif":
                aktif_obj.append(obj)
            else:
                tau_obj.append(obj)
                
        saveFile(pasif_obj,"D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/pasif_objek.json")
        saveFile(aktif_obj,"D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/entahlah_objek.json")
        saveFile(tau_obj,"D:/2023/Semester 3/Grafika Komputer/Tugas Akhir/PyGrafBuilder/PyGrafBuilder/resources/objek grafis/aktif_objek.json")





