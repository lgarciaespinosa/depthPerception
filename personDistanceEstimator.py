from Disparity_map_generator_HC import generateDisparityMap
from disparityCalculator import disparityCalculator
from distanceEstimator import estimateDistance
from distanceEstimatorPerspective import estimateDistanceFromPerspective
import keypointsToMask as k2m
from matrixLoader import get_perspective_matrix,normalize_coordinates
import cv2 as cv

alpha = 55.0
imgLenght = 480
imgWidth = 640

class PersonDistanceEstimator:
    def __init__(self, imgLeft, imgRight) :
        self.disparityMap = generateDisparityMap(imgLeft, imgRight)
    
    def getDistance(self,mask,person):
        if(person.hasFeet()):
            #getFeetPosition debe devolver el promedio de la posición de los pies capturados por cam1
            normalizedCoords = normalize_coordinates(person.getFeetPosition())
            return estimateDistanceFromPerspective(normalizedCoords)
        else:
            gsValues, cX, cY,_ = disparityCalculator(self.disparityMap, mask)
            print([cX,cY])
            
            estimatedDistance = estimateDistance(gsValues)
            
            if cX >= imgWidth/2:
                distanceFromCenter = -0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
            else:
                distanceFromCenter = 0.521 * estimatedDistance * 1/(imgWidth/2) * (cX - (imgWidth/2))
            
            
            return distanceFromCenter,estimatedDistance
        