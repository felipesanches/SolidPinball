# Flipper for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

#TAITO flipper dimensions:
# L=75.5
# R=15.5
# r=7.7

class Flipper(PinballPart):

  def __init__(self, angle=35, L=90, R=10, r=5, H=24, h=8, rubber_r=4, rubber_color="black", playfield_thickness=DEFAULT_PF_THICKNESS, segments=40):
    PinballPart.__init__(self, playfield_thickness, segments)
    self.angle = angle
    self.L = L
    self.R = R
    self.r = r
    self.H = H
    self.h = h
    self.rubber_r = rubber_r
    self.rubber_color = rubber_color

  def mount_holes_2d(self):
    return circle(r=6, segments=self.segments);

  def part_model(self):
    return self.flipper_shaft() + \
    rotate([0,0,self.angle])(
      self.flipper_body(),
      self.flipper_rubber()
    )

  def flipper_body(self):
	  return difference()(
		  union()(
			  linear_extrude(height=self.H)(
  			  self.flipper_outline(self.L, self.R, self.r)
        ),

			  linear_extrude(height=self.h)(
  			  self.flipper_outline(self.L + 2*self.rubber_r,
                               self.R + self.rubber_r,
                               self.r + self.rubber_r)
        )
		  )
	
		  #TODO hole for metalic axis
		  #translate([0,0,...])
		  #cylinder(r=..., h=...);
	  )

  def flipper_rubber(self):
    return \
    color(self.rubber_color)(
      translate([0, 0, self.h])(
	      linear_extrude(height=self.H - self.h)(
	        difference()(
          	self.flipper_outline(self.L + 2*self.rubber_r,
                            self.R + self.rubber_r,
                            self.r + self.rubber_r),
		        self.flipper_outline(self.L, self.R, self.r)
	        )
        )
      )
    )

  def flipper_shaft(self, radius=5.9/2, length=50):
    return \
    color("grey")( #metalic color
      translate([0,0,-length])(
        cylinder(r=radius, h=length, segments=20)
      )
    )

  def flipper_outline(self, L, R, r):
    return \
    hull()(
  		circle(r=R),
  		translate([L-r-R,0])(
    		circle(r=r)
      )
  	)

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Flipper(angle = -30), [100,100])
  pf.append(Flipper(angle = 180+30), [300,100])

  scad_render_to_file( pf.assembly(), 'flipper_example.scad')

