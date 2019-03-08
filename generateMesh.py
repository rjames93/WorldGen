import pymesh
import numpy as np
import random
import math

def generateMesh(n_points):
    points = [] # Simple 2D for initial testing

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
    meshgen.points = nppoints;
    meshgen.merge_coplanar = False
    meshgen.verbosity = 0
    meshgen.run()

    #mesh = pymesh.subdivide(meshgen.mesh, order = 1, method="loop")
    mesh = meshgen.mesh
    return(mesh)
