"""
.. py:module:: TuMAGtools.ObsCount_finder
.. module:: utils
        :platform: Unix
        :synopsis: Function for finding the images corresponding to a specific Observation Count and generate a new folder with them.  

        Command line execution :

            python/python3 ObsCount_finder.py Path_to_folder ObsCounter New_path
        
            Params:
                - Path_to_image : Path to a .img file.
                - ObsCounter : Int corresponding to the ObservationCounter variable in the header. 
                - New_path : Path of the new folder 

.. moduleauthor:: Pablo Santamarina  (SPG - IAA) <psanta@iaa.es>
"""
# ============================ IMPORTS ====================================== #

# Built-in libs 
import os
import sys
import glob
import numpy as np

# Own libs
from utils import read_Tumag
 

# =========================================================================== #

def obscount_finder(Folder, ObsCount, NewFolder):
    
    """
    Function that finds all images within a folder with a specific Observation 
    Counter and moves them to another one.
    
    Params :
        - Folder : Path to the folder containing the images
        - ObsCount : (int) Observation Counter
        - lp : Path to the new folder (can be a pre-existent one or not).
        
    """
    
    print('Selected Params:')
    print('Folder : ', Folder)
    print('Observation Counter : ', ObsCount)
    print('New Folder : ', NewFolder)
    
    All_images = sorted(glob.glob(os.path.join(Folder, '*')))

    print(f"Number of images found in folder: {len(All_images)}.")
    
    ObservationCounters = []
    obscount_images = []
    print("Reading images...")
    for img in All_images:
        H = read_Tumag(img, onlyheader= True) 
        oc = H["Observation_Counter"]
        if oc == ObsCount:
            obscount_images.append(img)
        elif oc not in ObservationCounters:
            ObservationCounters.append(oc)
        else:
            pass

    if len(obscount_images) < 1:
        print(f"0 images found for Observation Counter: {ObsCount}")
        print(f"Try an Observation Counter of : {ObservationCounters}")

    else:
        print(f"Found : {len(obscount_images)} images for Observation Counter {ObsCount}")
        print(f"Moving files into {NewFolder}...")
        if not os.path.isdir(NewFolder):
            os.mkdir(NewFolder)
        
        count = 0
        for img in obscount_images:
            os.rename(img, f"{NewFolder}/{os.path.basename(img)}")
            count += 1
        print(f"Moved {count} files.")

if __name__ == "__main__":
     
    args = sys.argv

    Folder = args[1]
    ObsCount = int(args[2])
    NewFolder = args[3]

    obscount_finder(Folder, ObsCount, NewFolder)
    
