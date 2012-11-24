# Ball hole for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class BallHole(PinballPart):

  def __init__(self, radius=15, **kwargs):
    super(BallHole, self).__init__(**kwargs)
    self.radius = radius

  def part_model(self):
    return None

  def mount_holes(self):
    epsilon = 0.1
    bevel_depth = self.playfield_thickness/2

    hole = \
    translate([0,0,-self.playfield_thickness-epsilon])(
      translate([0,0,bevel_depth])(
        cylinder(r1 = self.radius,
                 r2 = self.radius + bevel_depth,
                 h = self.playfield_thickness - bevel_depth + 2*epsilon)
      ),

      cylinder(r=self.radius, h=self.playfield_thickness + 2*epsilon)
    )
    return hole

  def mount_holes_2d(self):
    #just in case someone wants to use 
    #simple 2d playfield holes without bevels...
    return \
    circle(r=self.radius)

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(BallHole(), [50,30])
  pf.append(BallHole(), [120,300])
  pf.append(BallHole(), [200,230])
  pf.append(BallHole(), [120,70])
  pf.append(BallHole(), [230,130])
  pf.append(BallHole(radius=25), [50,140])

  scad_render_to_file( pf.assembly(), '/tmp/ballhole_example.scad')

