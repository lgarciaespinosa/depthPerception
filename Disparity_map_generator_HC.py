import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def generateDisparityMap(img_L, img_R):
    imgL = img_L
    imgR = img_R
    
    stereo = cv.StereoSGBM_create(numDisparities=16, blockSize=15)
    """
    Number of disparities (numDisparities): 
    Sets the range of disparity values to be searched. 
    The overall range is from minimum disparity value to minimum disparity value + number of disparities. 
    The following pair of images shows the disparity map calculated for two different disparity ranges. 
    It is clearly visible that increasing the number of disparitieimgR_undistorteds increases the accuracy of the disparity map
    """
    numDisparities = 4

    """
    Size of the sliding window used for block matching to find corresponding pixels in a rectified stereo image pair. 
    A higher value indicates a larger window size. increasing this parameter results in more smooth disparity maps.
    """
    blockSize = 2

    """
    Parameter to decide the type of pre-filtering to be applied to the images before passing to the block matching 
    algorithm. This step enhances the texture information and improves the results of the 
    block matching algorithm
    """
    #preFilterType = 1

    """Window size of the filter used in the pre-filtering stage"""
    #preFilterSize = 10

    #Limits the filtered output to a specific value.
    preFilterCap = 15

    #Filters out areas that do not have enough texture information for reliable matching
    #textureThreshold = 63

    """
    Another post-filtering step. If the best matching disparity is not sufficiently better than every other 
    disparity in the search range, the pixel is filtered out. Increasing 
    the uniqueness ratio increases the number of pixels that are filtered out.
    """
    uniquenessRatio = 8

    #defines how close the disparity values should be to be considered as part of the same blob
    speckleRange = 2

    #number of pixels below which a disparity blob is dismissed as “speckle”.
    speckleWindowSize = 10

    # defines the maximum allowable difference between the original left pixel and the back-matched pixel
    disp12MaxDiff = 0

    """The minimum value of the disparity to be searched. 
    In most scenarios it is set to zero. It can also be set to negative value depending on the stereo camera setup."""
    minDisparity = 0
    
    p1 = 7
    
    p2 = 203
    
    mode = 1

    stereo.setNumDisparities(numDisparities*16)
    stereo.setBlockSize(blockSize*2+5)
    #stereo.setPreFilterType(preFilterType)
    #stereo.setPreFilterSize(preFilterSize*2+5)
    stereo.setPreFilterCap(preFilterCap)
    #stereo.setTextureThreshold(textureThreshold)
    stereo.setUniquenessRatio(uniquenessRatio)
    stereo.setSpeckleRange(speckleRange)
    stereo.setSpeckleWindowSize(speckleWindowSize*2)
    stereo.setDisp12MaxDiff(disp12MaxDiff)
    stereo.setMinDisparity(minDisparity)
    stereo.setP1(p1)
    stereo.setP2(p2)
    stereo.setMode(mode)
    
    disparity = stereo.compute(imgL,imgR).astype(np.float32)
    disparity = disparity.astype(np.float32)
    disparity = (disparity/16.0 - minDisparity)/(numDisparities/16)
    return disparity