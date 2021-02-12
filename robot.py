import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, atan2, sqrt, pow, asin, pi

theta1 = 0.0
d1 = 0.0
a1 = 0.0
alpha1 = 0.0
theta2 = 0.0
d2 = 0.0
a2 = 0.0
alpha2 = 0.0
theta3 = 0.0
d3 = 0.0
a3 = 0.0
alpha3 = 0.0

vertices = (
    (0, 4, 0),
    (0.1, 4, 0),
    (0, 0, 0),
    (0.1, 0, 0),
    (0, 4, 0.1),
    (0.1, 4, 0.1),
    (0, 0, 0.1),
    (0.1, 0, 0.1)
)
verticesx = (
    (0, 3, 0),
    (0.1, 3, 0),
    (0, 0, 0),
    (0.1, 0, 0),
    (0, 3, 0.1),
    (0.1, 3, 0.1),
    (0, 0, 0.1),
    (0.1, 0, 0.1)
)
vertices2 = (
    (0, 2, 0),
    (0.1, 2, 0),
    (0, 0, 0),
    (0.1, 0, 0),
    (0, 2, 0.1),
    (0.1, 2, 0.1),
    (0, 0, 0.1),
    (0.1, 0, 0.1)
)
vertices3 = (
    (0, 1, 0),
    (0.1, 1, 0),
    (0, 0, 0),
    (0.1, 0, 0),
    (0, 1, 0.1),
    (0.1, 1, 0.1),
    (0, 0, 0.1),
    (0.1, 0, 0.1)
)

edges = (
    (0, 1),
    (0, 2),
    (0, 4),
    (3, 1),
    (3, 2),
    (3, 7),
    (5, 4),
    (5, 1),
    (5, 7),
    (6, 7),
    (6, 2),
    (6, 4)
)
surfaces = (
    (0, 1, 3, 2),
    (1, 3, 7, 5),
    (4, 5, 7, 6),
    (0, 2, 6, 4),
    (0, 1, 5, 4),
    (2, 3, 7, 6)
)
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1)
)


def drawText(position, text_string):
    font = pygame.font.Font(None, 32)
    text_surface = font.render(text_string, True, (255, 255, 255, 255), (0, 0, 0, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)


def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def cubex():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticesx[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticesx[vertex])
    glEnd()


def cube2():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices2[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices2[vertex])
    glEnd()


def cube3():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices3[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices3[vertex])
    glEnd()


def sphere():
    for i in range(0, 100 + 1):
        lat0 = pi * (-0.5 + float(float(i - 1) / float(100)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / float(100)))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)

        for j in range(0, 100 + 1):
            lng = 2 * pi * float(float(j - 1) / float(100))
            x = cos(lng)
            y = sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)

        glEnd()


def cylinder():
    half_length = 1
    radius = 1
    for i in range(200):
        theta = i * 2.0 * pi
        next_theta = i+1 * 2.0 * pi
        glBegin(GL_TRIANGLE_STRIP)
        glVertex3f(0.0, half_length, 0.0)
        glVertex3f(radius * cos(theta), half_length, radius * sin(theta))
        glVertex3f(radius * cos(next_theta), half_length, radius * sin(next_theta))
        glVertex3f(radius * cos(next_theta), -half_length, radius * sin(next_theta))
        glVertex3f(radius * cos(theta), -half_length, radius * sin(theta))
        glVertex3f(0.0, -half_length, 0.0)
        glEnd()


def main():
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    j4 = 0.0

    x1 = 0
    y1 = 0
    z1 = 0
    working_area = True
    shape = True
    kinematics = False
    move = False
    pygame.init()

    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, -2.0, -12.0)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j2 += 10.0
                    j2 = j2 % 360
                if event.key == pygame.K_RIGHT:
                    j2 -= 10.0
                    j2 = j2 % 360
                if event.key == pygame.K_DOWN:
                    j1 += 0.1
                    if j1 >= 2:
                        j1 = 2
                if event.key == pygame.K_UP:
                    j1 -= 0.1
                    if j1 <= 0:
                        j1 = 0
                if event.key == pygame.K_a:
                    j3 += 0.1
                    if j3 >= 1:
                        j3 = 1
                if event.key == pygame.K_d:
                    j3 -= 0.1
                    if j3 <= 0:
                        j3 = 0
                if event.key == pygame.K_s:
                    working_area = not working_area
                if event.key == pygame.K_w:
                    shape = not shape
                if event.key == pygame.K_q:
                    kinematics = True
                if event.key == pygame.K_e:
                    move = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glRotatef(j4, 0, -1, 0)
                    glTranslatef(0.0, 0.0, 1.0)
                    glRotatef(j4, 0, 1, 0)
                if event.button == 5:
                    glRotatef(j4, 0, -1, 0)
                    glTranslatef(0.0, 0.0, -1.0)
                    glRotatef(j4, 0, 1, 0)
                if event.button == 1:
                    j4 += 10
                    glRotatef(10, 0, 1, 0)
                if event.button == 3:
                    j4 -= 10
                    glRotatef(10, 0, -1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if working_area:
            if shape:
                glPushMatrix()
                glTranslatef(3.0 + 0.05, 1.9, 0)
                cylinder()
                glPopMatrix()
            else:
                glPushMatrix()
                glTranslatef(3.0 + 0.05, 1.9, 0)
                sphere()
                glPopMatrix()

        if kinematics:
            x1 = float(input("x1 [-1:1]"))
            var1 = sqrt(1-pow(x1, 2))
            z1 = float(input("y1 [-1:1]"))
            y1 = float(input("z1 max %.2f" % var1))
            kinematics = False
        x = cos(j2*pi/180)*(-j3+1)
        y = 1-j1
        z = sin(j2*pi/180)*(-j3+1)

        r = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
        phi = atan2(-z, x) * 180 / pi
        if not r == 0:
            theta = asin(y / r) * 180 / pi
        else:
            theta = 0

        j1_ = 1 - y1
        j2_ = atan2(z1, x1)
        if j2_ - pi/2 == 0 or j2_ + pi/2 == 0:
            j3_ = z1/sin(j2_)-1
        else:
            j3_ = -x1/cos(j2_) + 1

        j2_ = j2_ * 180/pi
        drawText((-9, 8, -5), "j1 = %.2f" % j1)
        drawText((-9, 7, -5), "j2 = %.2f degrees" % j2)
        drawText((-9, 6, -5), "j3 = %.2f" % j3)
        if move:
            j1 = j1_
            j2 = j2_
            j3 = j3_
            move = False
        else:
            drawText((-9, 2, -5), "j1_ = %.2f" % j1_)
            drawText((-9, 1, -5), "j2_ = %.2f degrees" % j2_)
            drawText((-9, 0, -5), "j3_ = %.2f" % j3_)
        if not shape:
            drawText((-9, 5, -5), "r = %.2f" % r)
            drawText((-9, 4, -5), "phi = %.2f" % phi)
            drawText((-9, 3, -5), "theta = %.2f" % theta)
        else:
            drawText((-9, 5, -5), "x = %.2f" % x)
            drawText((-9, 4, -5), "y = %.2f" % z)
            drawText((-9, 3, -5), "z = %.2f" % y)

        cube()

        glPushMatrix()
        glTranslatef(0.0, 4.0, 0.0)
        glRotatef(90.0, 0, 0, -1.0)
        cubex()
        glPopMatrix()
        glPushMatrix()
        glTranslatef(3.0, 2.9-j1+1, 0.0)
        cube2()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(3.0 + 0.05, 2.9 - j1+1, 0.0)
        glRotatef(90, 0.0, 0.0, -1)
        glRotatef(j2, 1, 0, 0)
        cube3()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4.0 + 0.05, 1.9 - j1+1, 0.0)
        glRotatef(90, 0, 0.0, -1)
        glTranslatef(0.0, -1, 0)
        glRotatef(j2, 1, 0, 0)
        glTranslatef(0.0, 1, 0)
        glRotatef(90, 0, 0, 1)
        cube3()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4.0 - j3 + 0.05, 1.9 - j1+1, 0.0)
        glRotatef(90, 0, 0.0, -1)
        glTranslatef(0, -1+j3, 0.0)
        glRotatef(j2, 1, 0, 0)
        glTranslatef(0, 1-j3, 0.0)
        cube2()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()
