import pymesh
import glfw
from OpenGL.GL import *


def renderLoop(mesh):

    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Planetoid Render", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):

        renderMesh(mesh)
        handleMovement()
        glClear(GL_COLOR_BUFFER_BIT)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

def createVBOs(mesh):
    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)

def renderMesh(mesh):
    print("Put the Mesh into the Environment")
    glClear(GL_COLOR_BUFFER_BIT)


def handleMovement():
    print("Handling Movement")
