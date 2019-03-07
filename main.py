#!./env/bin/python

import pymesh
import pyrender
import numpy as np
import trimesh
import random
import math

points = np.array([[]]) # Simple 2D for initial testing


n_points = 1000


for i in range(n_points):
    r = random.uniform(1.0,1.1)
    theta = random.uniform(0,math.pi)
    phi = random.uniform(0,math.pi * 2)
   
    x= r * math.sin(theta) * math.cos(phi)
    y= r * math.sin(theta) * math.sin(phi)
    z= r * math.cos(theta)
    points = np.append(points,[[x,y,z]])

# Now just to check we have the target number of unique points
print(points)

meshgen = pymesh.tetgen();
meshgen.points = points;
meshgen.verbosity = 2
meshgen.run()

mesh = meshgen.mesh

pymesh.save_mesh("output.stl", mesh)


tm = trimesh.load('output.stl')

tm.show()
