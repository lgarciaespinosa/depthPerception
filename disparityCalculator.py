import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
from collections import OrderedDict
import json
from JSONParser import load_json,parse_detected_person_json

def disparityCalculator(disparityMap, points):
    mask = np.zeros(disparityMap.shape[:2], np.uint8)
    if (len(points) == 4):
        pts = np.array(points, np.int32) 
        pts = pts.reshape((-1,1,2))
        
        cv.fillPoly(mask, [pts], 255)
    else:
        mask = mask + 255 * points
        
    
    
    hist_mask = cv.calcHist([disparityMap],[0],mask,[256],[1,255.0])
    return float(np.argmax(hist_mask))