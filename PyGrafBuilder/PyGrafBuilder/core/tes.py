from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from graphics import OpenGLInitializer
from ProjectManajer import ObjectManager,colors
from animation import Transform, Animation

def main():
    object_manager = ObjectManager()
    transform = Transform(object_manager.get_objects())
    animation = Animation(transform)
    window = OpenGLInitializer(object_manager=object_manager,transform=transform,window_size=[720,720],window_title="ini title",kiri=0,kanan=1000,atas=1000,bawah=0)
    
    # object_manager.create_circle(100,100,10,color=colors["Red"])
    # object_manager.create_circle(200,200,10,color=colors["Red"])
    object_manager.create_rectangle(100,100,100,50)
    object_manager.create_rectangle(230,100,100,50,name="kotak",color=colors["Blue"])
    animation.transform.scale(2,name="kotak")
    
    
    glutMainLoop()

if __name__ == "__main__":
    Main = main() 