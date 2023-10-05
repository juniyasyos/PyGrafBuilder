from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class GLWindow:
    def __init__(self,width=100,height=100,title="Window title") -> None:
        self.width = width
        self.height = height
        self.title = title

        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow(self.title)

        glEnable(GL_DEPTH_TEST)
    
    def run(self):
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Tambahkan kode render di sini
        glutSwapBuffers()

    def reshape(self, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.width / self.height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

    def keyboard(self, key, x, y):
        if key == b'\x1b':
            # Tombol 'ESC' untuk keluar
            sys.exit()
if __name__ == "__main__":
    window = GLWindow(800, 600, "OpenGL Window")
    window.run()