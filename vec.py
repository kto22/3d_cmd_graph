from vec3 import vec3
from vec2 import vec2

from math import sqrt, fabs, cos, sin


def clamp(n: int, smallest: int, largest: int) -> int:
    return max(smallest, min(n, largest))


def dot(a: vec3, b: vec3) -> float:
    return a.x * b.x + a.y * b.y + a.z * b.z


def sign(v: vec3) -> vec3:
    return vec3((0 < v.x) - (v.x < 0), (0 < v.y) - (v.y < 0), (0 < v.z) - (v.z < 0))


def step(edge: vec3, v: vec3) -> vec3:
    return vec3((edge.x < v.x), (edge.y < v.y), (edge.z < v.z))


def reflect(rd: vec3, n: vec3) -> vec3:
    x0 = rd.x - n.x * (2 * dot(n, rd))
    y0 = rd.y - n.y * (2 * dot(n, rd))
    z0 = rd.z - n.z * (2 * dot(n, rd))
    return vec3(x0, y0, z0)


def antiZero(n):
    if n == 0:
        return 1
    return n


def abs(v: vec3):
    return vec3(fabs(v.x), fabs(v.y), fabs(v.z))


def rotateX(a: vec3, angle) -> vec3:
    b = a
    b.z = a.z * cos(angle) - a.y * sin(angle)
    b.y = a.z * sin(angle) + a.y * cos(angle)
    return b


def rotateY(a: vec3, angle) -> vec3:
    b = a
    b.x = a.x * cos(angle) - a.z * sin(angle)
    b.z = a.x * sin(angle) + a.z * cos(angle)
    return b


def rotateZ(a: vec3, angle) -> vec3:
    b = a
    b.x = a.x * cos(angle) - a.y * sin(angle)
    b.y = a.x * sin(angle) + a.y * cos(angle)
    return b


def sphere(ro: vec3, rd: vec3, r) -> vec2:
    b = dot(ro, rd)
    c = dot(ro, ro) - r*r
    h = b*b-c
    if h < 0:
        return vec2(-1, -1)
    h = sqrt(h)
    return vec2(-b-h, -b+h)


def cube(ro: vec3, rd: vec3, boxSize: vec3, outNormal: vec3):

    m = vec3(1/antiZero(rd.x), 1/antiZero(rd.y), 1/antiZero(rd.z))
    n = vec3(m.x*ro.x, m.y*ro.y, m.z*ro.z)
    k = abs(vec3(m.x*boxSize.x, m.y*boxSize.y, m.z*boxSize.z))
    t1 = vec3(-n.x-k.x, -n.y-k.y, -n.z-k.z)
    t2 = vec3(-n.x + k.x, -n.y + k.y, -n.z + k.z)
    tN = max(max(t1.x, t1.y), t1.z)
    tF = min(min(t2.x, t2.y), t2.z)
    if tN > tF or tF < 0:
        return vec2(-1, -1)
    yzx = vec3(t1.y, t1.z, t1.x)
    zxy = vec3(t1.z, t1.x, t1.y)
    x0 = -sign(rd).x * step(yzx, t1).x * step(zxy, t1).x
    y0 = -sign(rd).y * step(yzx, t1).y * step(zxy, t1).y
    z0 = -sign(rd).z * step(yzx, t1).z * step(zxy, t1).z
    outNormal = vec3(x0, y0, z0)
    return vec2(tN, tF)


def plane(ro: vec3, rd: vec3, p: vec3, w: float):
    return -(dot(ro, p) + w) / dot(rd, p)
