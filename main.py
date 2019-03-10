#!./env/bin/python

import pymesh
import numpy as np
import random
import math
import uuid
import sys
from generateMesh import generateMesh
from continents import Continent, genContinents
from render import renderLoop, renderMesh


# Generate a spherical mesh to be used for the basis of the planetoid
mesh = generateMesh(10000)
mesh.enable_connectivity()

# Now we want to make continents. Continents will be used to add noise to the simulation (basic techtonics)
continents = genContinents(mesh)


# Pepper the mesh with some craters... This is gonna be a toughie but I'll figure it out



# Set a water depth. Maybe calculate the depth of the water by the %age of faces need to be above it?

# Now we want to do some smoothing across the surface. Rainfall simulation stuff

# Now we want to render the result

renderLoop(mesh)
