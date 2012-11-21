# A popbumper for a pinball machine
#
# This is part of the SolidPinball library:
#  a digital fabrication framework for pinball manufacturing 
#
# (c)2012 Felipe Sanches <fsanches@metamaquina.com.br>
# licensed under GPLv3 or later

from pyopenscad import *
from pinball.utils import *
from pinball.parts.PinballPart import PinballPart

#----------------------------------------------------
# pop bumper cap used in the MSDOS version
# of the Party Land playfield

def partyland_msdos_popbumper_cap(cap_color="grey", R=75/2, r=43/2, H=10):
  border_thickness=2
  d = 10
  border = 2
  h = (r-border)*(r-border)/(2*d) - d/2

  cap = \
  color(cap_color)(
    difference()(
      union()(
        cylinder(r=R, h=border_thickness),
        translate([0,0,border_thickness])(
          cylinder(r1=R, r2=r, h=H)
        )
      ),

      #spherical cut on top of the cap
      translate([0,0,H + h + border_thickness])(
        sphere(r=h+d, segments = 80)
      )
    )
  )

  return cap

#----------------------------------------------------
#pop bumper cap used in the Amiga version
# of the Stones'n'Bones playfield

def stonesnbones_amiga_popbumper_cap(R=40, r=18, height=15):
  part1 = \
	color([1,1,1])(
	  translate([0,0,0.4])(
	    intersection()(
		    difference()(
			    cylinder(h=height, r1=R, r2=r),
			    cylinder(h=height+1, r=r)
		    ),
		    linear_extrude(height=height+1)(
      		star(r0=r+5, r1=R-1, n=12)
        )
	    )
    )
  )

  part2 = \
	color([0,0.6,0])(
	  difference()(
		  cylinder(h=height, r1=R, r2=r),
		  translate([0, 0, height-1])(
  		  cylinder(h=10, r=r-2)
      )
	  )
  )

  return \
  union()(
    part1,
    part2
  )

#----------------------------------------------------
#pop bumper cap used in the MS-DOS version
# of the Stones'n'Bones playfield

def stonesnbones_msdos_popbumper_cap(R=40, r=18.0, height=15):
  h=5.0

  cap = \
  difference()(
    scale([1,1,float(height)/float(R)])(
		  sphere(r=R)
    ),

	  translate([0, 0, height])(
      scale([1,1,float(h)/float(r)])(
  		  sphere(r=r)
      )
    ),

    translate([-R, -R, -height])(
      cube([2*R, 2*R, height])
    )
  )

  part1 = \
	color([0.8,1,0.8])(
  	translate([0,0,0.4])(
    	intersection()(
		    difference()(
          cap,
			    cylinder(h=height, r=r)
		    ),
		    linear_extrude(height=height+1)(
		      star(r0=r+5, r1=R-1, n=8)
        )
	    )
    )
  )

  part2 = \
	color([0.7,0.5,0.7])(
    cap
  )

  return \
  union()(
    part1,
    part2
  )

#----------------------------------------------------
def popbumper_cap(game, version, capcolor):
  if (game=="stonesnbones"):
    if (version=="amiga"):
      return stonesnbones_amiga_popbumper_cap()

    if (version=="msdos"):
      return stonesnbones_msdos_popbumper_cap()

  if (game=="partyland"):
    return partyland_msdos_popbumper_cap(capcolor)

#----------------------------------------------------

class PopBumper(PinballPart):

  def __init__(self, game="partyland", version="msdos", cap_color="black", wafer_color="beige", hit_ring_height=35, playfield_thickness=DEFAULT_PF_THICKNESS, segments=40):
    PinballPart.__init__(self, playfield_thickness, segments)
    self.game = game
    self.version = version
    self.cap_color = cap_color
    self.wafer_color = wafer_color
    self.hit_ring_height = hit_ring_height

  def part_model(self):
    return union()(
      translate([0,0,self.hit_ring_height + 2])( #TODO: correct height
        popbumper_cap(self.game, self.version, self.cap_color)
      ),

      translate([0,0,self.hit_ring_height])( #TODO: check the correct height of the hit_ring
        self.popbumper_hit_ring()
      ),

      self.popbumper_body(),

      translate([0,0,3])(
        color(self.wafer_color)(
          self.popbumper_wafer()
        )
      ),

      self.popbumper_spring(),
      self.popbumper_spring_holder(),
      self.popbumper_screws(),

      translate([0,0, -self.playfield_thickness])(
        self.popbumper_mount_support(),
        self.popbumper_solenoid()
      )
    )

  def popbumper_mount_support(self):
    return empty_3d() #TODO: implement-me!
        
  def mount_holes_2d(self):
    holes = circle(r=4, segments = 40)

    for i in [0,180]:
      holes += rotate([0,0,i])(
        translate([17.5,0,0])(
          circle(r=3.5, segments = 40)
        )
      )

      holes += rotate([0,0,-45+i])(
        translate([11.5,0,0])(
          circle(r=2, segments = 40)
        )
      )

    return holes

  def mount_holes(self):
    '''3D description of the cut to be made in the playfield wood'''
    r=8
    H=9.3

    holes = \
    translate([0,0,-self.playfield_thickness-1])(
      linear_extrude(height=self.playfield_thickness+2)(
        self.mount_holes_2d()
      )
    )

    holes += \
    translate([0,0,-H])(
      cylinder(r=r, h=H+1, segments = 20)
    )

    return holes

  def popbumper_hit_ring(self, leg_length=77, ring_height=10):
    legs = empty_3d()
    for i in [-1,1]:
      legs += \
      translate([i*35/2, 0, -leg_length-ring_height])(
        cylinder(r=5/2, h=leg_length, segments = 20)
      )

    ring_base = \
    linear_extrude(height=1)(
      union()(
        difference()(
          circle(r=46/2, segments = 20),
          circle(r=46/2-2, segments = 20)
        ),
        translate([-35/2, 0])(
          circle(r=9/2, segments = 20)
        ),
        translate([35/2, 0])(
          circle(r=9/2, segments = 20)
        )
      )
    )

    ring = \
    difference()(
      cylinder(r1=46/2, r2=62/2, h=ring_height, segments = 40),
      translate([0, 0, -0.1])(
        cylinder(r1=46/2-1, r2=62/2-1, h=ring_height+0.2, segments = 40)
      )
    )

    hit_ring = \
    color("silver")(
      render()(
        legs,

        translate([0, 0, -ring_height])(
          ring,
          ring_base
        )
      )
    )
    return hit_ring

  def popbumper_body(self):
    return empty_3d() #TODO: implement-me!

  def popbumper_wafer(self):
    #WMS part no. 03-6035-XX (a.k.a. Bumper Wafer)
    stick_cone_length=11
    stick_length=40.68
    basedisc_height=2.2
    basedisc_r1=29.7
    basedisc_r2=21.3

    base_disc = cylinder(r1=basedisc_r1, r2=basedisc_r2, h=basedisc_height, segments = 60)

    stick_cone = \
    translate([0,0,-stick_cone_length])(
      cylinder(r1=2.15,r2=5.05, h=stick_cone_length, segments = 30)
    )

    thin_stick = \
    translate([0,0,-stick_length])(
      cylinder(r1=1.6,r2=2.15, h=stick_length-stick_cone_length, segments = 60)
    )

    #center holes
    holes = \
    translate([0,0,2.13])(
      cylinder(r=2.54,h=10)
    )

    holes += \
    translate([0,0,3.9])(
      cylinder(r=3.25,h=10)
    )

    #holes for hitring & lamp wiring
    for step in range(4):
      holes += \
      rotate([0,0,45+step*90])(
        translate([11,0,-1])(
          cylinder(r=5.5,h=10)
        )
      )

    #holes for screws
    for step in [1,2]:
      holes += \
      rotate([0,0,step*180])(
        translate([17.15,0,-1])(
          cylinder(r=4.25,h=10)
        )
      )

    wafer = \
    render()(
      difference()(
        union()(
          base_disc,
          stick_cone,
          thin_stick,

          #center
          cylinder(r=4.9,h=5.2, segments = 60)
        ),

        holes
      )
    )
    return wafer

  def popbumper_spring(self):
    return empty_3d() #TODO: Implement-me!

  def popbumper_spring_holder(self, R=17.5, r=8, H=9.3,h=7):
    holes = empty_3d()
    
    for i in range(4):
      holes += \
      rotate([0,0,45+i*90])(
        translate([R,0,-1])(
          cylinder(r=4,h=4)
        )
      )

    spring_holder = \
    render()(
      rotate([0,0,45])(
        difference()(
          union()(
            cylinder(r=R, h=2, segments = 30),

            translate([0,0,2-H])(
              cylinder(r=r, h=H, segments = 30)
            ),

            translate([11,0,0])(
              cylinder(r=7/2, h=h, segments = 30)
            ),

            translate([-11,0,0])(
              cylinder(r=7/2, h=h, segments = 30)
            )
          ),

          translate([0,0,4-H])(
            cylinder(r=r-2, h=H, segments = 30)
          ),

          translate([0,0,-H])(
            cylinder(r=r-3, h=H, segments = 30)
          ),

          translate([11,0,2])(
            cylinder(r=7/2-1, h=h, segments = 30)
          ),

          translate([-11,0,2])(
            cylinder(r=7/2-1, h=h, segments = 30)
          ),

          translate([11,0,-1])(
            cylinder(r=3/2, h=h+2, segments = 30)
          ),

          translate([-11,0,-1])(
            cylinder(r=3/2, h=h+2, segments = 30)
          ),

          holes,

          translate([0,11,-1])(
            cylinder(r=5/2, h=4, segments = 30)
          ),

          translate([0,-11,-1])(
            cylinder(r=5/2, h=4, segments = 30)
          ),

          translate([0,11,1])(
            cylinder(r=9.3/2, h=4, segments = 30)
          ),

          translate([0,-11,1])(
            cylinder(r=9.3/2, h=4, segments = 30)
          )
        )
      )
    )
    return spring_holder

  def popbumper_screws(self):
    return empty_3d() #TODO: implement-me!

  def popbumper_solenoid(self):
    return empty_3d() #TODO: implement-me!

  def popbumper_footprint(self):
    '''2D footprint of the part'''
    return empty_2d() #TODO: implement-me!

if __name__ == '__main__':
  from pinball.playfield import Playfield

  pf = Playfield(400,600)
  pf.append(PopBumper(game="partyland", version="msdos", cap_color="darkred"), [150,180])
  pf.append(PopBumper(game="stonesnbones", version="amiga"), [250,100])
  pf.append(PopBumper(game="stonesnbones", version="msdos"), [350,180])

  scad_render_to_file( pf.assembly(), '/tmp/popbumper_example.scad')

