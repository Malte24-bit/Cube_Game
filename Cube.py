import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (-0.5,  0.5,  0.5),
    (-0.5,  0.5, -0.5),
    ( 0.5,  0.5, -0.5),
    ( 0.5,  0.5,  0.5),
    (-0.5, -0.5, -0.5),
    ( 0.5, -0.5, -0.5),
    (-0.5, -0.5,  0.5),
    ( 0.5, -0.5,  0.5)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (7, 6),
    (6, 4),
    (0, 6),
    (1, 4),
    (2, 5),
    (3, 7)
)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0,0,-5)

    glRotatef(20,0,0,0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
quit()