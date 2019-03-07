#!env/bin/python

import pymesh
import pyrender
import numpy as np


points = np.array([ [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0] ]) # Simple 2D for initial testing

triangulation = pymesh.triangle();
triangulation.points = points;

triangulation.max_area = 0.05
triangulation.split_boundary = false;

triangulation.run()

mesh = triangulation.mesh;

m = pyrender.Mesg.from_trimesg(mesh)

