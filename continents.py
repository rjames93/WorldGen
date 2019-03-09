import pymesh
import numpy as np
import sys

class Continent:
    faces = []
    nFaces = 0
    mesh = None

    def __init__(self,continentid,startface):
        self.faces.append(startface)
        self.id = continentid

    def stepFill(self):
        # Get an array of the IDs of all the adjacent faces
        adjfaces = []
        for curface in self.faces:
            adjfaces.extend( self.mesh.get_face_adjacent_faces( curface ) )
        # Get the current continent ID array
        continentIDtoFace = self.mesh.get_face_attribute("continentID")        
        np.set_printoptions(threshold=sys.maxsize)
        # Create a temporary copy of said attributes
        tmp = continentIDtoFace[:].copy()

        # Now we need change the attribute on the new adjfaces to reflect the correct id
        for adjface in adjfaces:
            if(self.id == 0.0):
                tmp[adjface] = int(self.id)
    
        # Set the attribute data back to the mesh
        self.mesh.set_attribute("continentID",tmp);

        self.faces.extend(adjfaces)
        self.faces = list(set(self.faces))
        print(self.faces)
