from OpenGL.GL import *
from OpenGL.GLUT import *
from ProjectManajer import *
from animation import *

class OpenGLInitializer:
    def __init__(self, window_size=(1280, 720), window_title="OpenGL Window", kiri=-500.0,kanan=500,atas=500,bawah=-500,z_start=0.0,z_end=1.0):
        self.window_size = window_size
        self.window_title = window_title
        self.fullscreen = False
        self.object_manager = ObjectManager()
        self.transform = Transform(self.object_manager.get_objects())
        self.kiri = kiri
        self.kanan = kanan
        self.atas = atas
        self.bawah = bawah
        self.z_start = z_start
        self.z_end = z_end
        self.initialize_window()

    def set_transformObject(self, obj):
        self.transform = Transform(obj)

    def initialize_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(*self.window_size)
        glutCreateWindow(self.window_title)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)

    def set_window_properties(self, size, title):
        self.window_size = size
        self.window_title = title

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            glutFullScreen()
        else:
            glutReshapeWindow(*self.window_size)
            glutPositionWindow(10, 10)

    def set_modelView(self):
        glLoadIdentity()
        glViewport(0, 0, *self.window_size)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(self.kiri, self.kanan, self.atas, self.bawah, self.z_start, self.z_end)

    def display(self):
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
        glutPostRedisplay()

    def add_animation(self, obj_name, animation_func, duration):
        obj = self.object_manager.get_objects()
        obj_to_anim = [o for o in obj if o['name'] == obj_name]
        for o in obj_to_anim:
            o['animation'] = Animation(animation_func, duration)
