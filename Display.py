# Display.py

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Pyramid import Pyramid
from Prism import Prism

class Display:
    def __init__(self):
        self.objects = [Cube(), Pyramid(), Prism()]
        self.current_object = 0
        self.object_count = len(self.objects)
        self.translation = [0, 0, 0]  # Initial translation offsets
        self.rotation = [0, 0, 0]     # Initial rotation angles
        self.scale = 1.0              # Initial uniform scale factor
        self.translation_speed = 0.1  # Translation speed
        self.rotation_speed = 5       # Rotation speed (degrees)
        self.scale_speed = 0.1        # Scaling speed

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.translation[0] -= self.translation_speed
        if keys[K_RIGHT]:
            self.translation[0] += self.translation_speed
        if keys[K_UP]:
            self.translation[1] += self.translation_speed
        if keys[K_DOWN]:
            self.translation[1] -= self.translation_speed
        if keys[K_q]:  # Move backward
            self.translation[2] += self.translation_speed
        if keys[K_e]:  # Move forward
            self.translation[2] -= self.translation_speed
        if keys[K_w]:  # Rotate up around x-axis
            self.rotation[0] += self.rotation_speed
        if keys[K_s]:  # Rotate down around x-axis
            self.rotation[0] -= self.rotation_speed
        if keys[K_a]:  # Rotate up around y-axis
            self.rotation[1] += self.rotation_speed
        if keys[K_d]:  # Rotate down around y-axis
            self.rotation[1] -= self.rotation_speed
        if keys[K_r]:  # Rotate up around z-axis
            self.rotation[2] += self.rotation_speed
        if keys[K_f]:  # Rotate down around z-axis
            self.rotation[2] -= self.rotation_speed
        if keys[K_z]:  # Scale up uniformly
            self.scale += self.scale_speed
        if keys[K_x]:  # Scale down uniformly
            self.scale = max(0.1, self.scale - self.scale_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Press ESC to quit
                    pygame.quit()
                    quit()
                if event.key == K_SPACE:   # Press SPACE to switch object
                    self.current_object = (self.current_object + 1) % self.object_count

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (800 / 600), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        # Apply translation for the current object
        glTranslatef(*self.translation)

        # Apply rotation for the current object
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

        # Apply uniform scaling for the current object
        glScalef(self.scale, self.scale, self.scale)

        # Center the object on the screen
        glPushMatrix()
        self.objects[self.current_object].draw()
        glPopMatrix()

        pygame.display.flip()

    def run(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        while True:
            self.handle_input()
            self.render()
            pygame.time.wait(10)
