#!/usr/bin/python

from PIL import Image
import numpy
import sys
from pysynth import *
import random

def main():
    args = sys.argv
    # print args

    image_filename = args[1]
    output_filename = args[2]
    seconds = int(args[3])

    image = numpy.array(Image.open(image_filename))
    shape = image.shape
    flattened = image.reshape(shape[0] * shape[1], shape[2])


    # print len(image)
    # print flattened

    notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'r']
    octaves = [2,3,4,5,6]
    durations = [-4, 4, 4, 8, 8, 16]
    num_notes = len(notes)
    num_octaves = len(octaves)
    num_durations = len(durations)

    song = []
    size = len(flattened)
    for i in range(seconds * 3):
        row = flattened[random.randrange(size)]
        octave = octaves[row[1] % num_octaves]
        duration = durations[row[2] % num_durations]
        note = notes[row[0] % num_notes]
        if note != "r":
            note += str(octave)
        song.append((note, duration))


    print song
    make_wav(song, fn = output_filename)




if __name__ == "__main__": main()
