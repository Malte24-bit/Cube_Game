import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Enemy:
    def __init__(self, x_pos, y_pos, z_pos, size, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.color = color
        self.size = size

    def draw(self, x_pos, y_pos):

        glPushMatrix()
        glTranslatef(x_pos, y_pos, 0.0)

        glColor3f(*self.color)
        
        glBegin(GL_QUADS)
        # Bottom-Left
        glTexCoord2f(0.0, 0.0)
        glVertex2f(-0.5, -0.5)

        # Bottom-Right
        glTexCoord2f(1.0, 0.0)
        glVertex2f(0.5, -0.5)

        # Top-Right
        glTexCoord2f(1.0, 1.0)
        glVertex2f(0.5, 0.5)

        # Top-Left
        glTexCoord2f(0.0, 1.0)
        glVertex2f(-0.5, 0.5)
        glEnd()

        glPopMatrix()



    


