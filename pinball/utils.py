# helper statements for the SolidPinball library
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *

inch=25.4
DEFAULT_PF_THICKNESS = 15

#These are ugly hacks. We got to figure out something better...
def empty_3d():
  return sphere(r=0)

def empty_2d():
  return circle(r=0)

