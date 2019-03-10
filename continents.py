import pymesh
import numpy as np
import sys
import random
import uuid

def genContinents(mesh):
    # Add the Continent ID attribute to the Mesh
    mesh.add_attribute("continentID")
    val = np.zeros(mesh.num_faces)
    mesh.set_attribute("continentID",val);

    
    nContinents = random.randint(4,12)
    Continents = []

    for x in range(nContinents):
        continentid = uuid.uuid4()
        randomFaceElementNumber = random.randint(0,len(mesh.faces))
        Continents.append(Continent(continentid,randomFaceElementNumber))
        Continents[x].mesh = mesh

    spaceRemain = True
    while spaceRemain == True:
        for continent in Continents:
            if( continent.stepFill() == False ):
                spaceRemain = False
            else:
                spaceRemain = True

    return Continents


class Continent:
    faces = []
    nFaces = 0
    mesh = None

    def __init__(self,continentid,startface):
        self.faces.append(startface)
        self.id = continentid
    
    def doesContain(self,faceID):
        if faceID in faces:
            return True
        else:
            return False

    def sizeOfContinent(self):
        size = 0.0
        self.mesh.add_attribute("face_area")
        facesizes = self.mesh.get_face_attribute("face_area")
        
        for face in self.faces:
            size += facesizes[face]
        return size


    def stepFill(self):
        # Get an array of the IDs of all the adjacent faces
        adjfaces = []
        for curface in self.faces:
            adjfaces.extend( self.mesh.get_face_adjacent_faces( curface ) )
        # Get the current continent ID array
        continentIDtoFace = self.mesh.get_face_attribute("continentID")        
        
        # Now to go and check how many of these adjfaces are currently unassigned and remove the ones already assigned

        newlist = [ x for x in adjfaces if continentIDtoFace[x] == 0.0 ]
        adjfaces = newlist
        del(newlist)

        # Return False if there are no more unassigned empty faces
        if len(adjfaces) == 0:
            return False
        
        # Create a temporary copy of said attributes
        tmp = continentIDtoFace[:].copy()

        # Now we need change the attribute on the new adjfaces to reflect the correct id
        for adjface in adjfaces:
            tmp[adjface] = int(self.id)
    
        # Set the attribute data back to the mesh
        self.mesh.set_attribute("continentID",tmp);

        self.faces.extend(adjfaces)
        self.faces = list(set(self.faces))
        return True
