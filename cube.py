
from vec import *
#from math import *
width = 237
height = 63

aspect = width/height
pixasp = 11/24
gradient = " .:!/(l1Z4H9W8$@"
gradientSize = len(gradient)-1

for t in range(1000):

    screen = [' '] * width * height
    s = ''
    light = vec3.norm(vec3(-0.5, 0.5, -1))
    spherePos = vec3(0, 3, 0)

    for i in range(width):
        for j in range(height):

            x = (i/width*2-1)*aspect*pixasp
            y = j/height*2-1
            uv = vec2(x, y)

            ro = vec3(-6, 0, 0)
            rd = vec3.norm(vec3(2, x, y))

            ro = rotateY(ro, 0.25)
            rd = rotateY(rd, 0.25)
            ro = rotateZ(ro, t * 0.01)
            rd = rotateZ(rd, t * 0.01)

            diff = 1

            for k in range(5):

                minIt = 99999
                intersection = sphere(vec3(ro.x-spherePos.x, ro.y-spherePos.y, ro.z-spherePos.z), rd, 1)
                n = vec3(0, 0, 0)
                albedo = 1

                if intersection.x > 0:
                    x0 = ro.x-spherePos.x+rd.x*intersection.x
                    y0 = ro.y - spherePos.y + rd.y * intersection.x
                    z0 = ro.z - spherePos.z + rd.z * intersection.x
                    itPoint = vec3(x0, y0, z0)
                    minIt = intersection.x
                    n = vec3.norm(itPoint)

                boxN = vec3(0, 0, 0)
                intersection = cube(ro, rd, vec3(1, 1, 1), boxN)
                if intersection.x > 0 and intersection.x < minIt:
                    minIt = intersection.x
                    n = boxN

                intersection = plane(ro, rd, vec3(0, 0, -1), 1)
                intersection = vec2(intersection, intersection)
                if intersection.x > 0 and intersection.x < minIt:
                    minIt = intersection.x
                    n = vec3(0, 0, -1)
                    albedo = 0.5

                if minIt < 99999:
                    diff *= (dot(n, light)*0.5 + 0.5)*albedo
                    x0 = ro.x + rd.x * (minIt - 0.01)
                    y0 = ro.y + rd.y * (minIt - 0.01)
                    z0 = ro.z + rd.z * (minIt - 0.01)
                    ro = vec3(x0, y0, z0)
                    rd = reflect(rd, n)

                else:
                    break

            color = int(diff*20)
            color = clamp(color, 0, gradientSize)
            pixel = gradient[color]
            screen[i + j * width] = pixel

    for i in range(width*height):
        s += screen[i]
    print(s, end='')

# "C:\cmd_3d_graph\cube.py"