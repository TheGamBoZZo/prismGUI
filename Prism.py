from OpenGL.GL import *

class Prism:
    def __init__(self):
        
        self.vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [0, -1, 1],
            [0, 1, 1]
        ]
        
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 4), (2, 5), (3, 5),
            (4, 5)
        ]


    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def translate(self, dx, dy, dz):
        # Translate cube by specified offsets
        self.translation[0] += dx
        self.translation[1] += dy
        self.translation[2] += dz

    def apply_translation(self):
        # Apply translation to the object
        glTranslatef(*self.translation)
