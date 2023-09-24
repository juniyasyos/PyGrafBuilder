from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ProjectManajer import *
from transformations import *

# Initialization and Window Configuration
class OpenGLInitializer:
    """
    Initializes and configures the OpenGL window.
    """
    def __init__(self, window_size=(1280, 720), window_title="OpenGL Window",kiri=0,kanan=1280,atas=0,bawah=720,z_start=0.0,z_end=1.0):
        self.window_size = window_size
        self.window_title = window_title
        self.fullscreen = False
        self.object_manager = ObjectManager()
        self.transform = Transform(self.object_manager.get_Objects())
        self.kiri=kiri
        self.kanan=kanan
        self.atas=atas
        self.bawah=bawah
        self.z_start=z_start
        self.z_end=z_end
        self.initialize_window()
        self.putar = 10

    def initialize_window(self):
        """
        Initialize the OpenGL window using the appropriate library (e.g., GLUT).
        """
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(*self.window_size)
        glutCreateWindow(self.window_title)
        glutDisplayFunc(self.display)
        
        glutKeyboardFunc(self.keyboard)

    def set_window_properties(self, size, title):
        """
        Set window properties such as size and title.

        Args:
            size (tuple): The size of the window in (width, height) format.
            title (str): The title of the window.
        """
        self.window_size = size
        self.window_title = title

    def toggle_fullscreen(self):
        """ set window to fullscreen """
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            glutFullScreen()
        else:
            glutReshapeWindow(*self.window_size)
            glutPositionWindow(10, 10)
    
    def set_modelView(self):
        """
        set window about transformation or viewport in openGL
        """
        glLoadIdentity()
        glViewport(0,0,self.window_size[0],self.window_size[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(self.kiri,self.kanan,self.atas,self.bawah,self.z_start,self.z_end)
        

    def display(self):
        """
        function for eksecution objek in objek_manajer  
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.set_modelView()
        self.object_manager.draw_object()
        glutSwapBuffers()

    def keyboard(self, key, x, y):
        if key == b'f':
            self.toggle_fullscreen()
            if self.fullscreen:
                print("Mode Layar Penuh Aktif")
            else:
                print("Mode Layar Penuh Nonaktif")
        if key == b'a':
            self.transform.translate(-100, 0, ["tiga","kotak"])
        if key == b'd':
            self.transform.translate(100, 0, ["tiga","kotak"])
        if key == b's':
            self.transform.translate(0, -100, ["tiga","kotak"])
        if key == b'w':
            self.transform.translate(0, 100, ["tiga","kotak"])
        if key == b'r':
            for i in range(90):
                self.transform.rotate(angle_degrees=i, name="tiga", center_x=600, center_y=300)
                self.display()
                time.sleep(0.03)
        glutPostRedisplay()
