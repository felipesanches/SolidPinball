# Stud for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2014 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

inches = 25.4

class Stud(PinballPart):

  def __init__(self, radius=0.4*inches, height=30, rubber_radius=2, rubber_position=20, rubber_height=5, **kwargs):
    super(Stud, self).__init__(**kwargs)
    self.radius = radius
    self.height = height
    self.rubber_radius = rubber_radius
    self.rubber_height = rubber_height
    self.rubber_position = rubber_position


  def part_model(self):
    stud = \
	color([0.7, 0.7, 0.7])(
		translate([0,0,-self.height])(
			cylinder(r=self.radius, h=2*self.height)
		)
	)
    return stud

  def mount_holes(self):
	return None

  def mount_holes_2d(self):
    return circle(r=self.radius, segments=self.segments)

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Stud(), [200,30])

  scad_render_to_file( pf.assembly(), '/tmp/stud_example.scad')

