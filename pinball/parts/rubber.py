# rubbers for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Rubber(PinballPart):

  def __init__(self, rubber_height=20, rubber_radius=3, posts=[[0,0,7], [50,0,7]], **kwargs):
    super(Rubber, self).__init__(**kwargs)
    self.rubber_height = float(rubber_height)
    self.rubber_radius = float(rubber_radius)
    self.posts = posts

  def part_model(self):
    #TODO: This minkowski operation is extremely slow to render in OpenSCAD.
    # We should consider an alternative implementation.
    rubber = \
    translate([0,0,self.rubber_height])(
      minkowski()(
        self.rubber_outline(),
        sphere(r=self.rubber_radius/2, segments=10)
      )
    )
    return rubber

  def rubber_outline(self):
    corners = empty_2d()
    for p in self.posts:
      corners += translate([p[0], p[1]])(
        circle(r=p[2], segments=20)
      )

    area = hull()(corners)

    outline = minkowski()(
      area,
      circle(r=epsilon, segments = 20)
    ) - area

    return linear_extrude(height=epsilon)(outline)

  def mount_holes(self):
    return None

  def mount_holes_2d(self):
    return None

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Rubber(), [50,30])

  scad_render_to_file( pf.assembly(), '/tmp/rubber_example.scad')

