# Ball launcher for a pinball machine playfield
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2014 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Launcher(PinballPart):

  def __init__(self, cut_length=40, cut_width=4, plunger_width=60, plunger_length=100, pf_thickness=30):
    self.pf_thickness = pf_thickness
    self.cut_length = cut_length
    self.cut_width = cut_width
    self.plunger_width = plunger_width + 0.1
    self.plunger_length = plunger_length + 0.1

  def mount_holes(self):
    '''3D description of the cut to be made in the playfield wood'''

    plunger_cut = \
    translate([-self.plunger_width/2, -self.plunger_length, -self.pf_thickness-1])(
		linear_extrude(height=self.pf_thickness+2)(
			square([self.plunger_width, self.plunger_length])
		)
	)

    ball_centering_cut = \
	translate([0,338,3])(
		scale([1,1,0.5])(
			rotate([90,0,0])(
				cylinder(h=410, r1=0, r2=20)
			)
		)
	)

    rollover_switch_cut = \
    translate([0,13,-self.pf_thickness-1])(
		linear_extrude(height=self.pf_thickness+2)(
			hull()(
				translate([0,+self.cut_length/2])( circle(r=self.cut_width/2, segments=20) ),
				translate([0,-self.cut_length/2])( circle(r=self.cut_width/2, segments=20) )
			)
		)
	)

    return plunger_cut + ball_centering_cut + rollover_switch_cut

  def part_model(self):
    return self.shooter_switch() + self.plunger()

  def shooter_switch(self):
    #TODO: Implement-me!
    return empty_3d()

  def plunger(self):
    #TODO: Implement-me!
    return empty_3d()

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Launcher(), [400 - 30, 100])

  scad_render_to_file( pf.assembly(), '/tmp/launcher_example.scad')

