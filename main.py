#!./env/bin/python

import pymesh
import pyrender
import numpy as np
import trimesh
import moderngl
import random
import math
import pyglet
from pyglet.gl import *

points = [] # Simple 2D for initial testing
n_points = 100000


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

meshgen = pymesh.tetgen();
meshgen.points = points;
meshgen.verbosity = 1
meshgen.run()

mesh = pymesh.subdivide(meshgen.mesh, order = 1, method="loop")



print(mesh.faces)

pymesh.save_mesh("output.stl", mesh) # For debugging purposes
tm = trimesh.load('output.stl')
pyrendermesh = pyrender.Mesh.from_trimesh(tm,smooth=False)
scene = pyrender.Scene()
scene.add(pyrendermesh)
pyrender.Viewer(scene, use_raymond_lighting=True)
