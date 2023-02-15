import cv2 as cv
from Estimator import *

imgL = cv.imread('/home/lucas/Descargas/Sensor estereoscópico/Sensor images/Experiments/Aisle experiment/Aisle Set/Set1/corregido/cam1_450.jpg',1)
imgR = cv.imread('/home/lucas/Descargas/Sensor estereoscópico/Sensor images/Experiments/Aisle experiment/Aisle Set/Set1/corregido/cam2_450.jpg',1)

cv_file = cv.FileStorage("/home/lucas/Descargas/Sensor estereoscópico/Sensor images/Rectificacion/params_py_sensor_1.xml", cv.FILE_STORAGE_READ)
Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
cv_file.release()

imgL_undistorted = cv.remap(imgL,Left_Stereo_Map_x, Left_Stereo_Map_y, cv.INTER_LINEAR, cv.BORDER_CONSTANT)
imgR_undistorted = cv.remap(imgR,Right_Stereo_Map_x, Right_Stereo_Map_y, cv.INTER_LINEAR, cv.BORDER_CONSTANT)


est = Estimator(imgL_undistorted,imgR_undistorted)
coords = [[298,312], [304, 244], [263, 245], [268, 312]]

print(len(coords))

print (Estimator.getDistance(est,coords))