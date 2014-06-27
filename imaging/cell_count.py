#!/usr/bin/python

import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage
import sys

dna = mahotas.imread(sys.argv[1])
gauss = int(sys.argv[2])
dnaf = ndimage.gaussian_filter(dna, gauss)
rmax = pymorph.regmax(dnaf)
T = mahotas.thresholding.otsu(dnaf)
labeled,nr_objects = ndimage.label(dnaf > T)
seeds,nr_nuclei = ndimage.label(rmax)
print nr_nuclei
pylab.imshow(pymorph.overlay(dna,rmax))
#pylab.jet()
pylab.show()
