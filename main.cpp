using namespace std;
#include <iostream>
#include <cmath>
#include <cstring>
#include <unistd.h>
#include <GLFW/glfw3.h>
#include "shapes.h"

int main(int argc, char **argv){
	GLFWwindow* window;

	/* Initialize the library */
	if (!glfwInit())
		return -1;

	/* Create a windowed mode window and its OpenGL context */
	window = glfwCreateWindow(640, 480, "OpenGL World Generator", NULL, NULL);
	if (!window){
		glfwTerminate();
		return -1;
	}

	/* Make the window's context current */
	glfwMakeContextCurrent(window);

	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

	/* Working stuff */
	IcoSphere object;
	if(argc == 2){
		object.addeddepth = strtol(argv[1],NULL,10);
	} else {
		object.addeddepth = 0;
	}

	glEnable(GL_CULL_FACE);

	glShadeModel(GL_SMOOTH);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_COLOR_MATERIAL);
	glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE);
	GLfloat light_position[] = { 1.0, 1.0, 1.0, 0.0 };
	glLightfv(GL_LIGHT0, GL_POSITION, light_position);
	glEnable(GL_COLOR_MATERIAL);

	/* Loop until the user closes the window */
	while (!glfwWindowShouldClose(window)){
		/* Render here */
		glRotatef(1.0,1,1,0);
		glClear( GL_COLOR_BUFFER_BIT);

		object.draw();
		/* Swap front and back buffers */
		glfwSwapBuffers(window);

		/* Poll for and process events */
		glfwPollEvents();
	}

	glfwTerminate();
	return 0;
}
