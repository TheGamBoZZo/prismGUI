from OpenGL.GL import *

class Cube:
    def __init__(self):
        
        self.vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
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
