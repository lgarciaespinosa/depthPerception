from Disparity_map_generator_HC import generateDisparityMap
from disparityCalculator import disparityCalculator
from distanceEstimator import estimateDistance

class Estimator:
    def __init__(self, imgLeft, imgRight) :
        self.disparityMap = generateDisparityMap(imgLeft, imgRight)
    
    def getDistance(self,coords):
        gsValues = disparityCalculator(self.disparityMap, coords)
        estimatedDistance = estimateDistance(gsValues)
        return estimatedDistance
