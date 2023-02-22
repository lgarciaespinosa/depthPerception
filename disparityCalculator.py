import numpy as np
import cv2 as cv

def disparityCalculator(disparityMap, points):
    mask = np.zeros(disparityMap.shape[:2], np.uint8)
    if (len(points) == 4):
        pts = np.array(points, np.int32) 
        pts = pts.reshape((-1,1,2))
        
        cv.fillPoly(mask, [pts], 255)
    else:
        mask = mask + 255 * points
        
    
    contours, hierarchy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    retX = retY = 0
    for c in contours:
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"])
        retX = cX
        cY = int(M["m01"] / M["m00"])
        retY = cY
    
        
    hist_mask = cv.calcHist([disparityMap],[0],mask,[256],[1,255.0])
    return float(np.argmax(hist_mask)),cX,cY