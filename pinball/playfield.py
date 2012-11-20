# Class representing a playfield for a pinball machine
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

  def append(self, part, position, rotation=0):
    part.position = position
    part.rotation = rotation
    self.parts.append(part)

  def wood(self):
    pf_wood = \
    translate([0,0, -self.thickness])(
      cube([self.width, self.height, self.thickness])
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

