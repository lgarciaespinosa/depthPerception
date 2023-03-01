from Disparity_map_generator_HC import generateDisparityMap
from disparityCalculator import disparityCalculator
from distanceEstimator import estimateDistance
import keypointsToMask as k2m
import cv2 as cv

alpha = 55.0
imgLenght = 480
imgWidth = 640

class Estimator:
    def __init__(self, imgLeft, imgRight) :
        self.disparityMap = generateDisparityMap(imgLeft, imgRight)
    
    def getDistance(self,mask):
        #figureMask = k2m.keypointsToMask(self.disparityMap.shape[:2], coords)
        gsValues, cX, cY, lowestPoint = disparityCalculator(self.disparityMap, mask)
        print(lowestPoint)
        
        estimatedDistance = estimateDistance(gsValues)
        
        if cX >= imgWidth/2:
            distanceFromCenter = -0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        else:
            distanceFromCenter = 0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        
        return distanceFromCenter,estimatedDistance
