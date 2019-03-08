#!./env/bin/python

import pymesh
import pyrender
import numpy as np
import trimesh
import random
import math
import pygame
import OpenGL


from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

points = [] # Simple 2D for initial testing
n_points = 10000


for i in range(n_points):
    r = random.gauss(1,0.05)

    theta = random.random() * math.pi
    phi = random.random() * math.pi * 2
  
    x= r * math.sin(theta) * math.cos(phi)
    y= r * math.sin(theta) * math.sin(phi)
    z= r * math.cos(theta)
    points.append([x,y,z])

# Now just to check we have the target number of unique points

nppoints = np.asarray(points)
print(nppoints)
meshgen = pymesh.tetgen();
meshgen.points = nppoints;
meshgen.verbosity = 0
meshgen.run()

#mesh = pymesh.subdivide(meshgen.mesh, order = 1, method="loop")
mesh = meshgen.mesh.normalize()


def renderObject():
    for face in mesh.faces:
        glBegin(GL_TRIANGLES)
        glVertex3f(face[0][0],face[0][1],face[0][2])
        glVertex3f(face[1][0],face[1][1],face[1][2])
        glVertex3f(face[2][0],face[2][1],face[2][2])
        glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    renderObject()
    pygame.display.flip()
    pygame.time.wait(10)

main()

pymesh.save_mesh("output.stl", mesh) # For debugging purposes
tm = trimesh.load('output.stl')
pyrendermesh = pyrender.Mesh.from_trimesh(tm,smooth=False)
scene = pyrender.Scene()
scene.add(pyrendermesh)
pyrender.Viewer(scene, use_raymond_lighting=True)
