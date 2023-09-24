from graphics import *


window = OpenGLInitializer()
window.object_manager.create_rectangle(500,200,200,200,name="kotak")
window.object_manager.create_line(0,0,500,200)
window.object_manager.create_line(1280,720,700,400)
window.object_manager.create_line(1280,0,700,200)
window.object_manager.create_line(0,720,500,400)

glutMainLoop()