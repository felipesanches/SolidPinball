# Class representing a playfield for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pinball.utils import *
from pyopenscad import *

class Playfield(object):
  def __init__(self, width, height, thickness=DEFAULT_PF_THICKNESS):
    self.width = width
    self.height = height
    self.thickness = thickness
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
      pf_wood -= translate(part.position)(
        rotate([0,0,part.rotation])(
          part.mount_holes()
        )
      )

    return pf_wood

  def assembly(self):
    asm = self.wood()

    for part in self.parts:
      asm += translate(part.position)(
        rotate([0,0,part.rotation])(
          part.part_model()
        )
      )
    return asm

