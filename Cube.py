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

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


def Cube():
    glBegin(GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():

    pygame.init()

    display = (800, 600)

    pygame.display.set_mode(
        display,
        DOUBLEBUF | OPENGL
    )

    # Perspektive
    gluPerspective(
        45, display[0] / display[1], 0.1, 50.0
    )

    glTranslatef(0, 0, -5)

    # Spielerposition
    cube_x = 0
    cube_y = 0

    # Spielgeschwindigkeit
    speed = 0.05


    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            cube_y += speed

        if keys[pygame.K_DOWN]:
            cube_y -= speed

        if keys[pygame.K_LEFT]:
            cube_x -= speed

        if keys[pygame.K_RIGHT]:
            cube_x += speed


        glClear(
            GL_COLOR_BUFFER_BIT |
            GL_DEPTH_BUFFER_BIT
        )


        glPushMatrix()

        # Cube an Spielerposition bewegen
        glTranslatef(
            cube_x,
            cube_y,
            0
        )

        Cube()

        print()

        glPopMatrix()

        pygame.display.flip()

        pygame.time.wait(10)


main()
quit()