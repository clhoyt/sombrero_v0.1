# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:21:54 2013

@author: cad
"""


from bragg_optics import *
from detectors import *

from sources import *
from optical_system import *

from rt_functions import *
from rt_visuals import *
#from VisualizationFunctions import *

# define components
source = SphericalSource(diameter=10e-6)
source.setGaussianSpectrum(4750.0,fwhm=65.0)

optic = SphericalBraggOptic(55e-3,18e-3,180.0e-3,twoD=2.828e-10)
optic.setGaussianReflectProfile(fwhm=1e-4)

detector = Detector(2e-2,1e-2)

# define the optical path
setup = RayPathSystem(source=source,optic=optic,detector=detector)
setup.setDiffractionOrder(1.0)
setup.setSourcePosition(800.0e-3,22.64)
setup.setDetectorPosition(90e-3,22.64)
#setup.setDetectorPositionOnRowland(22.64)
#setup.setDetectorAtSagFocus()

# trace thru the system
#grid_trace_system(setup,hpoints=500,vpoints=500)
random_trace_system(setup,nrays=1e5)
optic_intercept_info(setup)
#detector_intercept_info(setup)
#mayavi_visual(setup)
#MayaviVisual(setup)
#SpectraImage(setup,bgNoise=False)

