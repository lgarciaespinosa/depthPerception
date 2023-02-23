import numpy as np
import cv2 as cv

def keypointsToMask(shape,points):
    #mask = np.zeros(disparityMap.shape[:2], np.uint8)
    mask = np.zeros(shape, np.uint8)
    pts = np.array(points, np.int32) 
    pts = pts.reshape((-1,1,2))
    
    cv.fillPoly(mask, [pts], 1)
    
    return mask
    