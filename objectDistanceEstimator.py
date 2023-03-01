from Disparity_map_generator_HC import generateDisparityMap
from disparityCalculator import disparityCalculator
from distanceEstimator import estimateDistance
from distanceEstimatorPerspective import estimateDistanceFromPerspective
from matrixLoader import normalize_coordinates

alpha = 55.0
imgLenght = 480
imgWidth = 640

class ObjectDistanceEstimator:
    def __init__(self, imgLeft, imgRight) :
        self.disparityMap = generateDisparityMap(imgLeft, imgRight)
    
    def getDistance(self,mask):
        gsValues, cX, cY, lowestPoint = disparityCalculator(self.disparityMap, mask)
        print([cX,cY])
        
        estimatedDistance = estimateDistance(gsValues)
        
        if cX >= imgWidth/2:
            distanceFromCenter = -0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        else:
            distanceFromCenter = 0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
        
        normalizedCoords = normalize_coordinates(lowestPoint)
        distanceFromCenterPersp, estimatedDistancePersp = estimateDistanceFromPerspective(normalizedCoords)
        
        return distanceFromCenter,estimatedDistance
            