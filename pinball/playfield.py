# Class representing a playfield for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pinball.utils import *
from solid import *

class Playfield(object):
  def __init__(self, width, height, position=[0,0,0], thickness=DEFAULT_PF_THICKNESS):
    self.width = width
    self.height = height
    self.thickness = thickness
    self.position = position
    self.parts = []

  def append_parts(self, parts):
    for item in parts:
      p = item['part']
      p.position = item['position']

      if 'rotation' in item.keys():
        p.rotation = item['rotation']
      else:
        p.rotation = 0
      self.parts.append(p)

  def append(self, part, position, rotation=0):
    part.position = position
    part.rotation = rotation
    self.parts.append(part)

  def wood(self):
    pf_wood = \
    color("BurlyWood")(
      translate([0,0, -self.thickness])(
        cube([self.width, self.height, self.thickness])
      )
    )

    for part in self.parts:
      if part.mount_holes():
        pf_wood -= translate(part.position)(
          rotate([0,0,part.rotation])(
            part.mount_holes()
          )
        )

    return translate(self.position)(pf_wood)

  def assembly(self):
    asm = self.wood()

    for part in self.parts:
      if part.part_model():
        asm += translate(part.position)(
          rotate([0,0,part.rotation])(
            part.part_model()
          )
        )
    return translate(self.position)(asm)

if __name__ == '__main__':
# This is an example on how to design a pinball playfield using SolidPinball.

  from pinball.parts.ballhole import BallHole
  from pinball.parts.flipper import Flipper 
  from pinball.parts.slingshot import Slingshot 
  from pinball.parts.popbumper import PopBumper
  from pinball.parts.laneguide import LaneGuideAssembly
  from pinball.parts.post import Post
  from pinball.parts.standuptarget import RoundStandupTarget, NarrowStandupTarget, WideStandupTarget
#TODO:  from pinball.parts.rubber import Rubber
#TODO:  from pinball.parts.droptarget import DropTarget

  pf_width = 600
  pf_height = 1200

  pf = Playfield(pf_width, pf_height)
  pf.append_parts([
    {'part': BallHole(), 'position': [pf_width/2,60] }, #ball drain
    {'part': BallHole(), 'position': [510, 720] },
    {'part': BallHole(), 'position': [200, 630] },
    {'part': BallHole(), 'position': [120, 670] },
    {'part': Flipper(angle=-42, rubber_color="orangered"), 'position': [pf_width/2 - 100, 200] },
    {'part': Flipper(angle=180+42, rubber_color="orangered"), 'position': [pf_width/2 + 100, 200] },
    {'part': Slingshot(angle=-70), 'position': [pf_width/2 - 130, 330] },
    {'part': Slingshot(angle=+70), 'position': [pf_width/2 + 130, 330] },
    {'part': PopBumper(cap_color="darkred"), 'position': [330, 630] },
    {'part': PopBumper(cap_color="darkblue"), 'position': [380, 690] },
    {'part': PopBumper(cap_color="darkgreen"), 'position': [410, 580] },
    {'part': LaneGuideAssembly(), 'position': [210, 920] },
    {'part': LaneGuideAssembly(), 'position': [260, 900] },
    {'part': LaneGuideAssembly(), 'position': [310, 920] },
    {'part': RoundStandupTarget(), 'position': [40, 820], 'rotation': 30 },
    {'part': NarrowStandupTarget(), 'position': [80, 840] },
    {'part': WideStandupTarget(), 'position': [120, 820], 'rotation': -30 },
    {'part': Post(), 'position': [360, 500] }
  ])

#This exports the design to a .scad file that you can render with OpenSCAD
#Available for download at www.openscad.org
  scad_render_to_file( pf.assembly(), '/tmp/playfield_assembly_example.scad')

# You may also try this to render only the playfield wood with the holes you need:
# Exporting it to an STL file you can CNC mill your own pinball playfield! 
  scad_render_to_file( pf.wood(), '/tmp/playfield_wood_example.scad')

