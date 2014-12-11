#ifndef SHAPES_H
#define SHAPES_H

using namespace std;

class IcoSphere{
	private:
		/* Stuff From the OpenGL tutorials on the internet */
		double X = 0.525731112119133606;
		double Z = 0.850650808352039932;
		unsigned int defaultfaces[20][3] = { {0,4,1}, {0,9,4}, {9,5,4}, {4,5,8}, {4,8,1}, {8,10,1}, {8,3,10}, {5,3,8}, {5,2,3}, {2,7,3}, {7,10,3}, {7,6,10}, {7,11,6}, {11,0,6}, {0,1,6}, {6,1,10}, {9,0,11}, {9,11,2}, {9,2,5}, {7,2,11} };
		double defaultvertices[12][3] = {{-X, 0.0, Z}, {X, 0.0, Z}, {-X, 0.0, -Z}, {X, 0.0, -Z},{0.0, Z, X}, {0.0, Z, -X}, {0.0, -Z, X}, {0.0, -Z, -X},{Z, X, 0.0}, {-Z, X, 0.0}, {Z, -X, 0.0}, {-Z, -X, 0.0} };
		const int defaultcolors[20][3] = {{237,108,54},{54,128,231},{134,204,122},{244,27,193},{105,79,23},{187,21,74},{124,26,121},{192,111,255},{219,154,114},{249,170,42},{175,174,229},{57,117,66},{118,27,19},{117,41,69},{22,78,146},{233,98,214},{240,66,22},{175,160,249},{242,138,185},{224,154,176}};

	public:
		double **vertices;
		double **normals;
		unsigned int **faces;
		
		unsigned int addeddepth;
		unsigned int n_faces;

		IcoSphere();
		void draw();
		void subdivide(double *, double *, double *, unsigned int );
	private:
		double phi = (1.0 + sqrt(5)) / 2.0;
};

void normalize(double v[3]);
void normcrossprod(double v1[3], double v2[3], double out[3]);
void drawtriangle(double *v1, double *v2, double *v3);
void framebuffer_size_callback(GLFWwindow* window, int width, int height);
#endif /* SHAPES_H */
