from OpenGL.GL import *

class Pyramid:
    def __init__(self):
        
        self.vertices = [
            [0, 1, 0],  # Top vertex
            [-1, -1, -1],  # Base vertices
            [1, -1, -1],
            [1, -1, 1],
            [-1, -1, 1]
        ]
        
        self.edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),  # Edges from the top vertex to the base vertices
            (1, 2), (2, 3), (3, 4), (4, 1)   # Base edges
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
