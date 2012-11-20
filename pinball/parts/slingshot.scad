

union() {
	union() {
		difference() {
			difference() {
				translate(v = [0, 0, -15]) {
					cube(size = [400, 600, 15]);
				}
				translate(v = [100, 100]) {
					rotate(a = [0, 0, 0]) {
						translate(v = [0, 0, -16]) {
							linear_extrude(height = 17) {
								rotate(a = [0, 0, 30]) {
									translate(v = [-30, 0]) {
										circle(r = 8);
									}
									translate(v = [-4, 0]) {
										hull() {
											translate(v = [0, -4]) {
												circle(r = 6);
											}
											translate(v = [0, 8]) {
												circle(r = 6);
											}
										}
									}
									translate(v = [30, 0]) {
										circle(r = 8);
									}
								}
							}
						}
					}
				}
			}
			translate(v = [300, 100]) {
				rotate(a = [0, 0, 0]) {
					translate(v = [0, 0, -16]) {
						linear_extrude(height = 17) {
							rotate(a = [0, 0, 150]) {
								translate(v = [-30, 0]) {
									circle(r = 8);
								}
								translate(v = [-4, 0]) {
									hull() {
										translate(v = [0, -4]) {
											circle(r = 6);
										}
										translate(v = [0, 8]) {
											circle(r = 6);
										}
									}
								}
								translate(v = [30, 0]) {
									circle(r = 8);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [100, 100]) {
			rotate(a = [0, 0, 0]) {
				cube(size = [0, 0, 0]);
			}
		}
	}
	translate(v = [300, 100]) {
		rotate(a = [0, 0, 0]) {
			cube(size = [0, 0, 0]);
		}
	}
}