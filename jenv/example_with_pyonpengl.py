from OpenGL.GL import *
from OpenGL.GLUT import *

# Hàm vẽ hình trái tim
def draw_heart():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Đặt màu đỏ
    # Đỉnh 1
    glVertex3f(0.0, 0.6, 0.0)
    # Đỉnh 2
    glVertex3f(-0.3, 0.0, 0.0)
    # Đỉnh 3
    glVertex3f(0.0, -0.6, 0.0)

    # Đỉnh 1
    glVertex3f(0.0, 0.6, 0.0)
    # Đỉnh 2
    glVertex3f(0.3, 0.0, 0.0)
    # Đỉnh 3
    glVertex3f(0.0, -0.6, 0.0)
    glEnd()

# Hàm vẽ
def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_heart()

    glutSwapBuffers()

# Hàm chính
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Hình trái tim bằng PyOpenGL")

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == "__main__":
    main()