import numpy as np
pts_src=np.array([[-18.5,-18.5,1],[18.5,-18.5,1],[18.5,18.5,1],[-18.5,18.5,1],[-18.5,101.5,1],[18.5,101.5,1],[18.5,138.5,1],[-18.5,138.5,1],[-18.5,221.5,1],[18.5,221.5,1],[18.5,258.5,1],[-18.5,258.5,1],[41.5,341.5,1],[78.5,341.5,1],[78.5,378.5,1],[41.5,378.5,1],[-138.5,221.5,1],[-101.5,221.5,1],[-101.5,258.5,1],[-138.5,258.5,1],[-138.5,101.5,1],[-101.5,101.5,1],[-101.5,138.5,1],[-138.5,138.5,1]])  # planar object points 
pts_dst=np.array([[663,451,1],[755,449,1],[740,388,1],[655,390,1],[636,274,1],[712,273,1],[702,234,1],[632,234,1],[620,158,1],[681,159,1],[676,133,1],[616,132,1],[693,81,1],[744,83,1],[735,64,1],[687,62,1],[421,162,1],[482,161,1],[485,133,1],[427,136,1],[392,279,1],[467,278,1],[471,236,1],[401,238,1]]) # image points
#finding homography
import cv2
h, status = cv2.findHomography(pts_src, pts_dst)
print(h)
im_src=cv2.imread('/home/rbc2080ti/Desktop/OpenCV/saved_img.jpg')
# warping source image to destination
im_dst = cv2.warpPerspective(pts_src, h, (pts_src.shape[1],pts_src.shape[0]))
# print(im_dst)
###################################################

pts_src=np.array([[-18.5],[101.5],[1]])  # planar object points 
h=np.array([[2.59275014,1.22742257,703.045769],[0.0176127956,-0.801686794,417.718048],[0.000208861672,0.00224224441,1.00000000]])
pts_dst=np.zeros((3,1)) # image points
#finding homography
import cv2
pts_dst=np.matmul(h,pts_src)
print(pts_dst)
# #,[-138.5,-78.5],[-101.5,-78.5],[-101.5,-41.5],[-138.5,-41.5]             ,[-41.5,341.5,0],[-41.5,378.5,0],[-78.5,378.5,0
