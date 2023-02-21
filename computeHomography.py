import numpy as np
pts_src=np.array([[-18.5,-18.5,1],[18.5,-18.5,1],[18.5,18.5,1],[-18.5,18.5,1],[-18.5,101.5,1],[18.5,101.5,1],[18.5,138.5,1],[-18.5,138.5,1],[-18.5,221.5,1],[18.5,221.5,1],[18.5,258.5,1],[-18.5,258.5,1],[41.5,341.5,1],[78.5,341.5,1],[78.5,378.5,1],[41.5,378.5,1],[-138.5,221.5,1],[-101.5,221.5,1],[-101.5,258.5,1],[-138.5,258.5,1],[-138.5,101.5,1],[-101.5,101.5,1],[-101.5,138.5,1],[-138.5,138.5,1]])  # planar object points 
pts_dst=np.array([[663,451,1],[755,449,1],[740,388,1],[655,390,1],[636,274,1],[712,273,1],[702,234,1],[632,234,1],[620,158,1],[681,159,1],[676,133,1],[616,132,1],[693,81,1],[744,83,1],[735,64,1],[687,62,1],[421,162,1],[482,161,1],[485,133,1],[427,136,1],[392,279,1],[467,278,1],[471,236,1],[401,238,1]]) # image points
import cv2
h, status = cv2.findHomography(pts_src, pts_dst)
# print(h)


pts_src=np.array([[-78.5,341.5],[-41.5,341.5],[-41.5,378.5],[-78.5,378.5],[-18.5,-18.5],[18.5,-18.5],[18.5,18.5],[-18.5,18.5]])  # planar object points 
print(np.shape(pts_src))
h=np.array([[2.59275014,1.22742257,703.045769],[0.0176127956,-0.801686794,417.718048],[0.000208861672,0.00224224441,1.00000000]])
pts_dst=np.zeros((3,1)) # image points
distortion_matrix = np.array([-0.44779831 , 0.21493212,0.0086979,-0.00269077,0.00281984])
camera_matrix = np.array([[931.82769928,0,645.03076458],[0,927.95336118,333.43480061],[0,0,1]])
print(np.shape(camera_matrix))
print(np.shape(distortion_matrix))
pts_src_1=[]
for pts in pts_src:
    # print(np.shape(pts))
    # print()
    pts=cv2.undistortPoints(pts,camera_matrix,distortion_matrix)
    print(np.shape(pts))
    print(pts)
    pts_src_1.append(pts)
dst=[]
# print(np.shape(pts_src_1))
import cv2,itertools
from numpy.linalg import inv
h=inv(h)
for pts in pts_src_1:
    # print(pts)
    
    # pts=pts.tolist()
    # # print(pts)
    # for p in pts:
    #     p[0].append(1)
        
    # print(pts)
    # pts=np.asarray(pts)
    np.append(pts,1)
    # print(pts)
    # print(np.shape(pts))
    # pts_dst=np.matmul(h,pts)
    # pts_dst[0]=pts_dst[0]/pts_dst[2]
    # pts_dst[1]=pts_dst[1]/pts_dst[2]
    # pts_dst[2]=1
    # dst.append(pts_dst)

# print("Hello")

# print(dst)
# img_test=np.array([[[523.0],[80.0]],[[576.0],[80.0]],[[574.0],[61.0]],[[525.0],[63.0]],[[663.0],[451.0]],[[755.0],[449.0]],[[740.0],[388.0]],[[655.0],[390.0]]])
# # print(img_test)
# img_test_1=[]

# for pts in img_test:
#     # print(pts)
#     # print()
#     pts=cv2.undistortPoints(np.array(pts),camera_matrix,distortion_matrix)
#     # print(pts)
#     img_test_1.append(pts)
# dist=0
# for pts_test,pts in zip(img_test_1,dst):
#     # print(pts_test)
#     # print()
#     # print(pts)
#     # pts_test=pts_test.tolist()
#     # # print(pts)
#     # pts_test.append([1])
#     # # print(pts)
#     # pts_test=np.array(pts_test)
    
#     for p1,p2 in zip(pts_test,pts):
#         #   print(p1[0],p2[0])
#           dist+=pow(abs(p1[0]-p2[0]),2)
          
#     # print(np.sqrt(dist))
# # #,[-138.5,-78.5],[-101.5,-78.5],[-101.5,-41.5],[-138.5,-41.5]             ,[-41.5,341.5,0],[-41.5,378.5,0],[-78.5,378.5,0
