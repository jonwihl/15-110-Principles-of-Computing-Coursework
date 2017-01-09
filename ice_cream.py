import math

def cone_volume(radius, height):
	c_volume = (1 / 3) * math.pi * radius ** 2 * height
	return c_volume

def sphere_volume(radius):
	s_volume = (4 / 3) * math.pi * radius ** 3
	return s_volume

def print_fraction_volume_wasted(x, y):
	return cone_volume(x, y)
	return sphere_volume(x)
	volume_wasted = volume / (sphere_volume + volume)
	print "The fraction of volume wasted is %lf" % volume_wasted


	