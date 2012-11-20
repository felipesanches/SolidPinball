# A lane guide for a pinball machine#
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class LaneGuide(PinballPart):
  #WMS part no. 03-8318-XX. Red is #03-8318-9

  def __init__(self, color="darkred", playfield_thickness=DEFAULT_PF_THICKNESS, segments=40):
    PinballPart.__init__(self, playfield_thickness, segments)
    self.color = color

    self.height=18.3;
    self.length=28.55;
    self.thickness=1.34;
    self.top_thickness=2;
    self.width=17.71-self.thickness;
    self.attachments_height = 5.3;

  def mount_holes_2d(self):
    return circle(r=0); #the lane itself does not require holes

  def part_model(self):
    return rotate([0,0,90])(
      color(self.color)(
        self.side_walls() +
        difference()(
          self.top() + self.screw_attachments(),
          self.screw_attachment_holes()
        )
      )
    )

  def side_walls(self):
    x=2.3
    walls = empty_3d()
    for i in [-1,1]:
      walls += \
      translate([0, self.thickness/2 + i*(self.width/2),0])(
        rotate([90,0,0])(
          linear_extrude(height=self.thickness)(
            polygon(points=[
                [-self.length/2 + x,  0],
                [-self.length/2,      self.height],
                [ self.length/2,      self.height],
                [ self.length/2 - x,  0]
            ])
          )
        )
      )

    return walls

  def screw_attachment_holes(self):
    holes = empty_3d()
    for i in [-1, 1]:
      holes += \
      translate([i*(self.length/2+1.5), 0, -self.attachments_height + self.height + self.top_thickness - 1])(
        cylinder(r=2.2, h=self.attachments_height + 2, segments=20),
        cylinder(r=4.7, h=self.attachments_height + 1 - self.thickness)
      )
    return holes

  def top(self):
    return \
    translate([0,0,self.height + self.top_thickness/2])(
      cube([self.length, self.width + self.thickness, self.top_thickness], center=True)
    )

  def screw_attachments(self):
    att = empty_3d()
    for i in [-1, 1]:
      att += \
      translate([i*(self.length/2+1.5),0,-self.attachments_height + self.height + self.top_thickness])(
        cylinder(r=6.2, h = self.attachments_height)
      )
    return att

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(LaneGuide(), [200,120])
  pf.append(LaneGuide(), [250,100])
  pf.append(LaneGuide(), [300,120])

  scad_render_to_file( pf.assembly(), '/tmp/laneguide_example.scad')

