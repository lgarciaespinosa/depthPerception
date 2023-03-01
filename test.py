import cv2 as cv
from Estimator import *
import keypointsToMask as k2m
from matrixLoader import get_perspective_matrix,normalize_coordinates
import numpy as np

imgL = cv.imread('Images/cam1_450.jpg',1)
imgR = cv.imread('Images/cam2_450.jpg',1)
cv.line(imgL, (320,0), (320,480), (255,255,255), 1) 

'''
cv.circle(imgL, (320, 240), 5, (255,255,255), -1)
cv.circle(imgR, (320, 240), 5, (255,255,255), -1)
cv.imshow("test", imgL)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("test", imgR)
cv.waitKey(0)
cv.destroyAllWindows()
'''

cv_file = cv.FileStorage("params_py_sensor_1.xml", cv.FILE_STORAGE_READ) 
Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
cv_file.release()

imgL_undistorted = cv.remap(imgL,Left_Stereo_Map_x, Left_Stereo_Map_y, cv.INTER_LINEAR, cv.BORDER_CONSTANT)
imgR_undistorted = cv.remap(imgR,Right_Stereo_Map_x, Right_Stereo_Map_y, cv.INTER_LINEAR, cv.BORDER_CONSTANT)


est = Estimator(imgL_undistorted,imgR_undistorted)
coords = [[298,312], [304, 244], [263, 245], [268, 312]]
left_feet =[295, 424]
right_feet = [282,432]

figureMask = k2m.keypointsToMask(imgL.shape[:2], coords)

matrix = get_perspective_matrix()
'''
x = (coords[0][0] + coords[3][0])/2
y = (coords[0][1] + coords[3][1])/2
'''
normalizedCoords = normalize_coordinates([(left_feet[0]+right_feet[0])/2,(left_feet[1]+right_feet[1])/2])

dot_product  = np.dot(matrix,  normalizedCoords)

x = dot_product[0]/dot_product[2]
y = dot_product[1]/dot_product[2]

'''
x_prima = (a1 * x + a2 * y + b1) /( c1*x + c2 * y + 1)
y_prima = (a3 * x + a4 * y + b2) /( c1*x + c2 * y + 1)
'''
print (x[0]/2000,y[0]/2000)
print (Estimator.getDistance(est,figureMask))
offset = 37
cv.line(imgL_undistorted, (320,0), (320,480), (0,0,0), 1) 
cv.line(imgL_undistorted, (288,0), (288,480), (0,0,255), 1)
cv.line(imgL_undistorted, (283,0), (283,480), (0,255,0), 1)

cv.imshow("test",imgL_undistorted)
cv.waitKey(0)
cv.destroyAllWindows()
'''
normalizedCoords = normalize_coordinates(Estimator.getDistance(est,figureMask))

dot_product  = np.dot(matrix,  normalizedCoords)

print (dot_product)
'''

