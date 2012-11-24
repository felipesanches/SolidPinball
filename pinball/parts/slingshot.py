# Slingshots for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Slingshot(PinballPart):

  def __init__(self, angle=60, **kwargs):
    super(Slingshot, self).__init__(**kwargs)
    self.angle = angle

  def part_model(self):
    #TODO: implement-me!
    return None

  def mount_holes_2d(self):
    radius = 8

    return \
    rotate([0,0,self.angle])(
      translate([-30,0])(
        circle(r=radius)
      ),

      translate([-4,0])(
        hull()(
          translate([0,-4])(
            circle(r=radius-2)
          ),

          translate([0,8])(
            circle(r=radius-2)
          )
        )
      ),

      translate([30,0])(
        circle(r=radius)
      )
    )

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Slingshot(angle = 30), [100,100])
  pf.append(Slingshot(angle = 180-30), [300,100])

  scad_render_to_file( pf.assembly(), '/tmp/slingshot_example.scad')

