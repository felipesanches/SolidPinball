# Post for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class StandupTarget(PinballPart):

  def __init__(self, thickness=2, target_color="orangered", target_height=1*inch, **kwargs):
    super(StandupTarget, self).__init__(**kwargs)
    self.thickness = thickness
    self.target_color = target_color
    self.target_height = target_height

  def part_model(self):
    return union()(
      self.target(),
      self.switch_body(),
      self.mounting()
    )

#  def mount_holes(self):
#    return None

  def target(self):
    #this must be implemented by inheriting classes
    return empty_3d()

  def switch_body(self):
    return empty_3d() #TODO: implement-me!

  def mounting(self):
    return empty_3d() #TODO: implement-me!

  def mount_holes_2d(self):
    holes = \
    minkowski()(
      projection(cut = True)(
        translate([0,0,-self.target_height])(
          self.target(),
          self.switch_body()
        )
      ),
      circle(r=4, segments = 20)
    )
    return holes

#-------------------------------------------------------------------------------
class RoundStandupTarget(StandupTarget):

  def __init__(self, radius=14, **kwargs):
    super(RoundStandupTarget,self).__init__(**kwargs)
    self.radius = radius

  def target(self):
    return \
    translate([0,0,self.target_height])(
      rotate([90, 0, 0])(
        cylinder(r=self.radius, h=self.thickness)
      )
    )

#-------------------------------------------------------------------------------
class RectangularStandupTarget(StandupTarget):

  def __init__(self, width, height, **kwargs):
    super(RectangularStandupTarget, self).__init__(**kwargs)
    self.width = width
    self.height = height

  def target(self):
    return \
      translate([0,0,self.target_height])(
        color(self.target_color)(
          difference()(
            cube([self.width, self.thickness, self.height], center=True),

            rotate([90,0,0])(
              cylinder(r=(1/8)*inch, h=2*self.thickness, segments=20, center=True)
            )
          )
        ) + \
        color("silver")(
          translate([0,-self.thickness/2])(
            scale([1,0.3,1])(
              sphere(r=(1/8*4/5)*inch, segments=20)
            )
          )
        )
      )

#-------------------------------------------------------------------------------
class WideStandupTarget(RectangularStandupTarget):

  def __init__(self, **kwargs):
    super(WideStandupTarget, self).__init__(width = (1 + 11.0/32)*inch, height = 1*inch, thickness = 3.0/8*inch, **kwargs)

class NarrowStandupTarget(RectangularStandupTarget):

  def __init__(self, **kwargs):
    #TODO: check dimensions
    super(NarrowStandupTarget, self).__init__(width = (3.0/4)*inch, height = 1*inch, thickness = 3.0/8*inch, **kwargs)

  def part_model(self):
    return \
    super(NarrowStandupTarget, self).part_model() 

class SquareStandupTarget(RectangularStandupTarget):

  def __init__(self, **kwargs):
    super(SquareStandupTarget, self).__init__(width = 1*inch, height = 1*inch, thickness = 3.0/8*inch, **kwargs)

  def part_model(self):
    return \
    super(SquareStandupTarget, self).part_model() 

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(RoundStandupTarget(), [50,30])
  pf.append(SquareStandupTarget(), [100,30])
  pf.append(NarrowStandupTarget(), [150,30])
  pf.append(WideStandupTarget(), [200,30])

  scad_render_to_file( pf.assembly(), '/tmp/standuptarget_example.scad')

