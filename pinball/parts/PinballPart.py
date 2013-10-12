# Class representing a generic part for a pinball machine
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *

class PinballPart(object):
  def __init__(self, playfield_thickness=DEFAULT_PF_THICKNESS, segments=40):
    self.segments = segments
    self.playfield_thickness = playfield_thickness
  
  def mount_holes_2d(self):
    '''2D description of the mounting hole shapes for this part.'''
    return None

  def mount_holes(self):
    '''These are the holes made to the playfield wood when installing this part. You may implement your own mount_holes() method if you want a 3d profile for your mounting holes. Otherwise, the default behaviour is to simply cut the hole based on the shapes described in the mount_hole_2d method'''
    if self.mount_holes_2d():
      return translate([0,0,-self.playfield_thickness-1])(
        linear_extrude(height=self.playfield_thickness+2)(
          self.mount_holes_2d()
        )
      )
    else:
      return None

