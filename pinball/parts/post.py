# Post for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Post(PinballPart):

  def __init__(self, radius=10, height=30, rubber_radius=2, rubber_height=20, **kwargs):
    super(Post, self).__init__(**kwargs)
    self.radius = radius
    self.height = height
    self.rubber_radius = rubber_radius
    self.rubber_height=rubber_height


  def part_model(self):
    R = self.radius
    r = R/2
    H = self.height
    h = H*24/30
    d=2

    post = \
    difference()(
      union()(
        cylinder(r1=R-d, r2=r, h=H),

        intersection()(
          cylinder(r1=R, r2=r+d, h=H),
          cube([2*R,2*R,2*h],center=True)
        )
      ),
      translate([0,0,-1])(
        cylinder(r=m4_diameter/2, h=H+2, segments=20)
      ),

      translate([0,0,self.rubber_height])(
        rotate_extrude()(
          translate([r+d + (H-self.rubber_height)*(R-r-d)/H,0])(
            circle(r=self.rubber_radius, segments=20)
          )
        )
      )
    )
    return post

  def mount_holes(self):
    return None

  def mount_holes_2d(self):
    return None

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Post(), [50,30])

  scad_render_to_file( pf.assembly(), '/tmp/post_example.scad')

