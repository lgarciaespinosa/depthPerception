from matrixLoader import get_perspective_matrix,normalize_coordinates
import numpy as np

pixelDensity = 2000

def estimateDistanceFromPerspective(lowestPoint):
    matrix = get_perspective_matrix()
    
    #getFeetPosition debe devolver el promedio de la posición de los pies capturados por cam1
    normalizedCoords = normalize_coordinates(lowestPoint)
    dot_product  = np.dot(matrix,  normalizedCoords)

    x = dot_product[0]/dot_product[2]
    y = dot_product[1]/dot_product[2]
    
    return x[0]/pixelDensity, y[0]/pixelDensity
    
    
    