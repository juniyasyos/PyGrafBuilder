from graphics import *
from ProjectManajer import *

window = OpenGLInitializer()
window.object_manager.create_rectangle(20,20,100,100,name="kotak")
window.transform.scale(8,name="kotak")

glutMainLoop()