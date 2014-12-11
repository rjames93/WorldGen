using namespace std;
#include <iostream>
#include <cmath>
#include <GLFW/glfw3.h>
#include "shapes.h"

void IcoSphere::subdivide(double *v1, double *v2, double *v3, unsigned int depth){

	double v12[3], v23[3], v31[3];

	if (depth == 0) {
		/* These are the lowest level vertices */
		/* Need to save these to the vertices object */
		//fprintf(stdout,"%lf	%lf	%lf\n",*v1,*v2,*v3);
		drawtriangle(v1, v2, v3);
		return;
	}

	for (unsigned int i = 0; i < 3; i++) {
		v12[i] = ( v1[i]+v2[i] ) / 2.0;
		v23[i] = ( v2[i]+v3[i] ) / 2.0;
		v31[i] = ( v3[i]+v1[i] ) / 2.0;
	}
	normalize(v12);
	normalize(v23);
	normalize(v31);

	subdivide(v1, v12, v31, depth-1);
	subdivide(v2, v23, v12, depth-1);
	subdivide(v3, v31, v23, depth-1);
	subdivide(v12, v23, v31, depth-1);

}

void IcoSphere::draw(){
	/*
	glBegin(GL_TRIANGLES);
	for(unsigned int i = 0; i < n_faces; i++){
		glNormal3dv(&vertices[faces[i][0]][0]); 
		glVertex3dv(&vertices[faces[i][0]][0]);

		glNormal3dv(&vertices[faces[i][1]][0]);
		glVertex3dv(&vertices[faces[i][1]][0]);

		glNormal3dv(&vertices[faces[i][2]][0]);
		glVertex3dv(&vertices[faces[i][2]][0]);

	}
	glEnd();
	*/
	
	/* Subdivision function is called on drawing because I'm lazy */
	for (unsigned int i = 0; i < 20; i++) {
		//glColor3ub(defaultcolors[19-i][0],defaultcolors[19-i][1],defaultcolors[19-i][2]);
		subdivide(&defaultvertices[defaultfaces[i][0]][0],&defaultvertices[defaultfaces[i][1]][0],&defaultvertices[defaultfaces[i][2]][0],addeddepth);
	}
}


IcoSphere::IcoSphere(){
	n_faces = 20;

	vertices = new double* [n_faces];
	for(unsigned int i = 0; i < n_faces; i++){
		vertices[i] = new double[3];
	}

	faces = new unsigned int *[n_faces];
	for(unsigned int i = 0; i < n_faces; i++){
		faces[i] = new unsigned int[3];
	}

	for(unsigned int i = 0; i < 12; i++){
		for(unsigned int j = 0; j < 3; j++){
			vertices[i][j] = defaultvertices[i][j];
		}
	}
	for(unsigned int i = 0; i < 20; i++){
		for(unsigned int j = 0; j < 3; j++){
			faces[i][j] = defaultfaces[i][j];
		}
	}


}
