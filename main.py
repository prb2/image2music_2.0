#!/usr/bin/python

from PIL import Image
import numpy
import sys

def main():
	args = sys.argv
	print args
	image_filename = args[1]
	# output_filename = args[2]
	image = numpy.array(Image.open(image_filename))
	flattened = image.reshape(761460, 3)
	print len(image)
	print flattened


if __name__ == "__main__": main()
