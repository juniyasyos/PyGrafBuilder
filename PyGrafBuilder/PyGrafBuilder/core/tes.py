from graphics import *


window = OpenGLInitializer()
# window.object_manager.set_objectsFile()
# window.transform.rotate(30,0,0,name="rectangle")
# window.transform.translate(100,0)
window.object_manager.create_triangle(100,100,100,name="tiga",color=colors["Cyan"])
# window.transform.rotate(20,100,80)
# for i in window.object_manager.get_Objects():
#     print(i)
glutMainLoop()