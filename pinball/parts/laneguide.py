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
from pinball.parts.post import Post

class LaneGuide(PinballPart):
  #WMS part no. 03-8318-XX. Red is #03-8318-9

  def __init__(self, color="darkred", **kwargs):
    super(LaneGuide, self).__init__(**kwargs)
    self.color = color

    #hardcoded parameters (should we have some of these as constructor params?)
    self.height=18.3;
    self.length=28.55;
    self.thickness=1.34;
    self.top_thickness=2;
    self.width=17.71-self.thickness;
    self.attachments_height = 5.3;

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

class LaneGuideAssembly(PinballPart): #create an Assembly class?!
  #TODO: add mount screws
  def __init__(self, **kwargs):
    super(LaneGuideAssembly,self).__init__(**kwargs)
    self.lguide = LaneGuide()
    self.p1 = Post()
    self.p2 = Post()

  def part_model(self):
    return \
    union()(
      self.laneguide(),
      self.posts()
    )

  def mount_holes(self):
    return None

  def laneguide(self):
    return \
    translate([0, 0, 14])(
      self.lguide.part_model()
    )

  def posts(self):
    return \
    union()(
      translate([0, self.lguide.length/2+1.5])(
        self.p1.part_model()
      ),
      translate([0, -self.lguide.length/2-1.5])(
        self.p2.part_model()
      )
    )

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(LaneGuideAssembly(), [200,120])
  pf.append(LaneGuideAssembly(), [250,100])
  pf.append(LaneGuideAssembly(), [300,120])

  scad_render_to_file( pf.assembly(), '/tmp/laneguide_example.scad')

