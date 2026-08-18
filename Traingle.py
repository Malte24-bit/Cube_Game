import Enemy

import pygame
from pygame.locals import *

import random

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
print(scaled_vertices)Traingle.py
"""

class Triangle:
    def __init__(self, x_pos, y_pos, z_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.color = color

    def draw(self):
        glPushMatrix()

        glTranslatef(self.x_pos, self.y_pos, 0)

        glColor3f(*self.color)

        glBegin(GL_TRIANGLES)
        
        for vertex_x, vertex_y in vertices:
            glVertex3f(vertex_x, vertex_y, 0)

        glEnd()

        glPopMatrix()



def main():
    pygame.init()
    
    display = (2048, 1080)
    enemies = []
    spawn_timer = 0
    SPAWN_RATE = 60


    triangle = Triangle(0, 0, 0, (0, 0, 1))
    
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
        # Perspektive
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    #object init
    

    while True:
        spawn_timer += 1
        if spawn_timer >= SPAWN_RATE:
            # Create a new quad enemy from your imported Enemy module
            # Replace 'QuadEnemyClass' with the actual class name inside Enemy.py
            random_x =  random.uniform(-3.0, 3.0)
            random_y =  random.uniform(-3.0, 3.0)
            new_enemy = Enemy.Enemy(0, 0, 0, 1, (0,0,1))
            enemies.append(new_enemy) # Add it to our active list           

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:    triangle.x_pos += 0.05
        if keys[pygame.K_LEFT]:     triangle.x_pos -= 0.05
        if keys[pygame.K_UP]:       triangle.y_pos += 0.05
        if keys[pygame.K_DOWN]:     triangle.y_pos -= 0.05
            
        
        
        # "boilerplate code"
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #traingle generate with the draw() method
        triangle.draw()

        for enemy in enemies:
            enemy.draw(enemy.x_pos, enemy.y_pos)

        pygame.display.flip()
        
        pygame.time.wait(15)


        
main()
quit()