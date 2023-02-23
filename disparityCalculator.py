import numpy as np
import cv2 as cv
#debe recibir una mascara de true/false
def disparityCalculator(disparityMap, inputMask):
    mask = np.zeros(disparityMap.shape[:2], np.uint8)
    thresholdMask = (inputMask > 0) * 255
    
    mask = np.uint8(mask + thresholdMask)
        
    
    contours, hierarchy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    
        
    hist_mask = cv.calcHist([disparityMap],[0],mask,[256],[1,255.0])
    return float(np.argmax(hist_mask)),cX,cY