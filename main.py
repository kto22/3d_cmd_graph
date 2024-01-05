
from vec import *
from math import *
width = 237
height = 63

aspect = width/height
pixasp = 11/24
gradient = " .:!/(l1Z4H9W8$@"
gradientSize = len(gradient)-1

for k in range(1000):
    screen = [' '] * width * height
    s = ''
    light = vec3.norm(vec3(sin(k*0.08), cos(k*0.08), -1))

    for i in range(width):
        for j in range(height):
            x = (i/width*2-1)*aspect*pixasp
            y = j/height*2-1
            uv = vec2(x, y)

            ro = vec3(-2, 0, 0)
            rd = vec3.norm(vec3(1, x, y))

            pixel = ' '
            color = 0
            intersection = sphere(ro, rd, 1)

            if intersection.x > 0:
                x0 = intersection.x
                itPoint = vec3(rd.x*x0+ro.x, rd.y*x0+ro.y, rd.z*x0+ro.z)
                n = vec3.norm(itPoint)
                diff = dot(n, light)
                color = int(diff * 20)

            color = clamp(color, 0, gradientSize)
            pixel = gradient[color]
            screen[i + j * width] = pixel

    for i in range(width*height):
        s += screen[i]
    print(s, end='')

# "C:\cmd_3d_graph\main.py"