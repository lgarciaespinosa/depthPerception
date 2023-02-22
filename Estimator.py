from Disparity_map_generator_HC import generateDisparityMap
from disparityCalculator import disparityCalculator
from distanceEstimator import estimateDistance
import cv2 as cv

alpha = 55.0
imgLenght = 480
imgWidth = 640

class Estimator:
    def __init__(self, imgLeft, imgRight) :
        self.disparityMap = generateDisparityMap(imgLeft, imgRight)
    
    def getDistance(self,coords):
        gsValues, cX, cY = disparityCalculator(self.disparityMap, coords)
        
        cv.circle(self.disparityMap, (320, 240), 5, (255,255,255), -1)
        
        cv.imshow("test", self.disparityMap/64)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
        estimatedDistance = estimateDistance(gsValues)
        
        if cX >= imgWidth/2:
            distanceFromCenter = -0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        else:
            distanceFromCenter = 0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        
        
        
        
        print(cX)
        print(cY)
        return estimatedDistance, distanceFromCenter
