from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from graphics import OpenGLInitializer
from ProjectManajer import ObjectManager
from animation import Transform, Animation

# Inisialisasi objek-objek dan window
window = OpenGLInitializer()
object_manager = ObjectManager()
transform = Transform(object_manager.get_objects())
animation = Animation(transform)

# Buat objek-objek (contoh: sebuah kotak)
object_manager.create_rectangle(0, 0, 100, 100, name="kotak")
animation.transform.rotate(angle_degrees=30,name="kotak")
animation.transform.scale(2,name="kotak")

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     object_manager.draw_object()
#     glutSwapBuffers()

# Callback untuk animasi (misalnya: pergerakan ke kanan saat tombol 'd' ditekan)
def keyboard_obj(key, x, y):
    if key == b'd':
        animation.move_object_right("kotak", distance=0.1)
        glutPostRedisplay()
    if key == b'a':
        animation.move_object_left("kotak", distance=0.1)
        glutPostRedisplay()
    if key == b'w':
        animation.move_object_up("kotak", distance=0.1)
        glutPostRedisplay()
    if key == b's':
        animation.move_object_down("kotak", distance=0.1)
        glutPostRedisplay()
    if key == b'r':
        animation.rotate_object_clockwise("kotak",angle_degrees=20)
        glutPostRedisplay()
    
# Callback untuk animasi pasif rotasi
def anime_rotation(a):
    angle_degrees = 0
    rotation_speed = 1.0  # Kecepatan rotasi (ubah sesuai kebutuhan)
    angle_step = rotation_speed * 360 / 60  # 60 FPS

    angle_degrees += angle_step
    animation.rotate_object_clockwise("kotak", angle_degrees=angle_step)
    glutPostRedisplay()
    glutTimerFunc(1000 // 60, anime_rotation, 0)  # 60 FPS


glutTimerFunc(0,anime_rotation,0)
glutKeyboardFunc(keyboard_obj)
glutMainLoop()
