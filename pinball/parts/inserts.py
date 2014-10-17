# Inserts of a pinball machine playfield
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2014 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from solid import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

class Inserts(PinballPart):

  def __init__(self, dxf, color=[0.5, 0.5, 0.7, 0.8], thickness=3, pf_thickness=30):
    # TODO: improve file path handling
    self.dxf = dxf
    self.color = color
    self.thickness = thickness
    self.pf_thickness = pf_thickness

  def mount_holes(self):
    '''3D description of the cut to be made in the playfield wood'''
    return translate([0,0,-self.thickness])(
        linear_extrude(height=self.thickness + 1)(
            import_(self.dxf)
        )
    ) + \
    translate([0,0,-self.pf_thickness])(
        linear_extrude(height=self.pf_thickness + 1)(
            import_(self.dxf) #TODO: calculate inset of this shape
        )
    )


  def part_model(self):
    return color(self.color)(
        translate([0,0,-self.thickness])(
            linear_extrude(height=self.thickness)(
                import_(self.dxf)
            )
        )
    )

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(Inserts("inserts_example.dxf")) #TODO: add an example DXF file

  scad_render_to_file( pf.assembly(), 'inserts_example.scad')

