# main.py
from Display import Display
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Pyramid import Pyramid
from Prism import Prism

def main():
    display = Display()
    display.run()
    
if __name__ == "__main__":
    main()
