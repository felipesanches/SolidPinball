# helper statements for the SolidPinball library
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from math import cos, sin, pi

inch=25.4
DEFAULT_PF_THICKNESS = 15
m3_diameter = 3
m4_diameter = 4
epsilon = 0.01

#These are ugly hacks. We got to figure out something better...
def empty_3d():
  return sphere(r=0)

def empty_2d():
  return circle(r=0)

def star(r0=3, r1=5, n=5.0):
  s = empty_2d()
  for i in range(n):
    s += polygon([[0,0],
    [r0*cos(i * 2*pi / float(n)), r0*sin(i * 2*pi / float(n))],
    [r1*cos(i * 2*pi / float(n) - pi/float(n)), r1*sin(i * 2*pi / float(n) - pi/float(n))],
    [r0*cos((i-1) * 2*pi / float(n)), r0*sin((i-1) * 2*pi / float(n))],
    [r0*cos(i * 2*pi / float(n)), r0*sin(i * 2*pi / float(n))]])
  return s


