# Rollover switch for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2014 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Rollover(PinballPart):

  def __init__(self, width=4, length=40, **kwargs):
    super(Rollover, self).__init__(**kwargs)
    self.width = width
    self.length = length

  def part_model(self):
	#TODO: Implement-me
    return empty_3d()

  def mount_holes_2d(self):
    return hull()(
		translate([0, +self.length/2])(circle(r=self.width/2, segments=30)),
		translate([0, -self.length/2])(circle(r=self.width/2, segments=30))
	)

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Rollover(), [50,30])

  scad_render_to_file( pf.assembly(), '/tmp/rollover_example.scad')

