#include <iostream>
#include <cmath>
#include <unistd.h>
#include <GLFW/glfw3.h>
#include "shapes.h"


void normalize(double v[3]) {    
	double d = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]); 
	if (d == 0.0) {
		fprintf(stderr,"zero length vector");    
		return;
	}
	v[0] /= d; v[1] /= d; v[2] /= d; 
}

void normcrossprod(double v1[3], double v2[3], double out[3]){ 
	out[0] = v1[1]*v2[2] - v1[2]*v2[1]; 
	out[1] = v1[2]*v2[0] - v1[0]*v2[2]; 
	out[2] = v1[0]*v2[1] - v1[1]*v2[0]; 
	normalize(out); 
}

void drawtriangle(double *v1, double *v2, double *v3){ 
	glBegin(GL_TRIANGLES); 
	glNormal3dv(v1); glVertex3dv(v1);    
	glNormal3dv(v2); glVertex3dv(v2);    
	glNormal3dv(v3); glVertex3dv(v3);    
	glEnd(); 
}

void framebuffer_size_callback(GLFWwindow* window, int width, int height){
	    glViewport(0, 0, width, height);
}
