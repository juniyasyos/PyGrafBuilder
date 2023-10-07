from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from graphics import OpenGLInitializer
from ProjectManajer import ObjectManager,colors
from animation import Transform, Animation
import random as rd

class android:
    def __init__(self,object_manager,animation):
        self.animation = animation
        object_manager.create_circle(0,0,150,name="head",opsi=0.5,color=colors['Green'],group=["android"])
        object_manager.create_circle(-60,-70,20,name="mata1",group=["android"])
        object_manager.create_circle(60,-70,20,name="mata2",group=["android"])

        object_manager.create_rectangle(-150,10,300,300,name="body",color=colors["Green"],group=["android"])
        object_manager.create_circle(-192,25,40,name="bahu1",color=colors["Green"],group=["android"])
        object_manager.create_circle(192,25,40,name="bahu2",color=colors["Green"],group=["android"])

        object_manager.create_rectangle(-231.5,15,79,170,name="lengan1",color=colors["Green"],group=["android"])
        object_manager.create_rectangle(152.5,15,79,170,name="lengan2",color=colors["Green"],group=["android"])

        object_manager.create_circle(-192,180,40,name="tangan1",color=colors["Green"],group=["android"])
        object_manager.create_circle(192,180,40,name="tangan2",color=colors["Green"],group=["android"])

        object_manager.create_rectangle(-121.5,250,79,170,name="kaki1",color=colors["Green"],group=["android"])
        object_manager.create_rectangle(42.5,250,79,170,name="kaki2",color=colors["Green"],group=["android"])

        object_manager.create_circle(-82,410,39,name="alas1",color=colors["Green"],group=["android"])
        object_manager.create_circle(82,410,39,name="alas2",color=colors["Green"],group=["android"])
        animation.transform.translate(390,500,name="android")
        
        glutTimerFunc(0,self.lengen_dada_dada,0)

    
    def lengen_dada_dada(self, value):
        if not hasattr(self, 'angle_degrees'):
            self.angle_degrees = 201
            self.rotation_speed = 1.0
            self.direction = 1 

        if self.angle_degrees >= 350 or self.angle_degrees <= 200:
            self.direction *= -1 
        
        angle_step = self.rotation_speed * self.direction
        self.angle_degrees += angle_step
        
        self.animation.rotate_object_clockwise("lengan1", angle_degrees=angle_step, center_x=-196, center_y=21)
        self.animation.rotate_object_clockwise("tangan1", angle_degrees=angle_step, center_x=-196, center_y=20)

        glutPostRedisplay()
        glutTimerFunc(1000 // 60, self.lengen_dada_dada, 0)
    
        
class xendit:
    def __init__(self,object_manager,animation):
        object_manager.create_polygon([(2.5110828365283,1.6948025938735),(1.5996653302464,3.2438182723229),(1.959497413408,3.2544015688864),(2.7,2)],name="xendit",color=colors["Blue"])
        object_manager.create_polygon([(1.5996653302464,3.2438182723229),(2.5,4.8),(2.7,4.5),(1.959497413408,3.2544015688864)],name="xendit",color=colors["Blue"])
        object_manager.create_polygon([(2.5,4.8),(3.4,4.8),(3.2,4.5),(2.7,4.5),(2.7,4.5)],name="xendit",color=colors["Blue"])

        # X
        object_manager.create_polygon([(2.7,4.5),(2.9581243868851,4.0631863646461),(2.766121510799,3.7685755875341),(2.5,4.2)],color=colors['Red'],name="xendit")
        object_manager.create_polygon([(2.5098288347141,2.312488174728),(2.7,2),(3.9741603345122,4.1918285461149),(3.7875298444594,4.4982030235776)],color=colors['Red'],name="xendit")
        object_manager.create_polygon([(3.5437625328962,2.4330239999353),(3.7145537791955,2.7264346025521),(3.9685510172818,2.319163169069),(3.8,2)],color=colors['Red'],name="xendit")

        # Tameng 2
        object_manager.create_polygon([(3.0970777348824,1.6973078620303),(3.9641717545561,1.6929285993046),(3.8,2),(3.2634897184562,1.9863392019215)],name="xendit",color=colors["Blue"])
        object_manager.create_polygon([(3.8,2),(3.9641717545561,1.6929285993046),(4.8865764970506,3.2644342475013),(4.5241599157606,3.2591818332797)],name="xendit",color=colors["Blue"])
        object_manager.create_polygon([(4.8865764970506,3.2644342475013),(4.5241599157606,3.2591818332797),(3.7875298444594,4.4982030235776),(3.9751578728795,4.8072397296619)],name="xendit",color=colors["Blue"])
        animation.transform.scale(100,name="xendit")
        animation.transform.translate(4,1,name="xendit")


def main():
    object_manager = ObjectManager()
    transform = Transform(object_manager.get_objects())
    animation = Animation(transform)
    window = OpenGLInitializer(object_manager=object_manager,transform=transform,window_size=[720,720],window_title="ini title",kiri=0,kanan=1000,atas=1000,bawah=0)
    android(object_manager,animation)
    xendit(object_manager,animation)
    
    glutMainLoop()

if __name__ == "__main__":
    Main = main() 


