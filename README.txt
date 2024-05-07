Python3 tools to analyze TuMag (and SCIP data). 

The following modules need to be installed in the python distribution: 
 - numpy
 - matplotlib
 - astropy
 - os
 - sys
 - glob
 - scipy

All tools can be run via terminal command. More info about the required arguments for each function at the start of each file. 

Description of the tools developed for the commisioning phase of TuMAG:

	- utils.py : Module with the function used to read Images and Thumbnails (.img) and obtain the header. This module can't be executed, only contains a function used in the other modules.

	- Imview.py : Module developed to visualize and analyze individual images.

	- VoltageScan.py : Module to visualize the mean value of a series of images as a function of the voltage applied to the etalon.

	- Photon_flux.py : Module used to visualize the mean value per accumulation of a series of images as a function of the exposure time.

	- focus_finder.py : Module developed to find the best focus, by fitting a parabola to the contrast values of a series of images of a through focus procedure.