import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1),
    (0.5,0),
    (-0.5,0)
    )
""" scale vertices
scaled_vertices = tuple(
    (x * 0.4, y * 0.4)
    for x, y in vertices
)
print(scaled_vertices)
"""

class Traingle:
    def __init__(self, x_pos, y_pos, z_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.color = color

    def draw(self):

        glColor3f(*self.color)
        glBegin(GL_TRIANGLES)
        for vertex_x, vertex_y in vertices:
            glVertex3f(vertex_x, vertex_y, 0)
        glEnd()



def main():
    pygame.init()
    
    display = (2048, 1080)
    
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
        # Perspektive
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    #object init
    triangle = Traingle(0, 0, 0, (0, 0, 1))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            glTranslatef(0.1, 0.0, 0.0)
        if keys[pygame.K_LEFT]:
            glTranslatef(-0.1, 0.0, 0.0)
        if keys[pygame.K_UP]:
            glTranslatef(0.0, 0.1, 0.0)
        if keys[pygame.K_DOWN]:
            glTranslatef(0.0, -0.1, 0.0)

        # "boilerplate code"
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #traingle generate with the draw() method
        triangle.draw()

        pygame.display.flip()
        
        pygame.time.wait(15)

        

main()
quit()