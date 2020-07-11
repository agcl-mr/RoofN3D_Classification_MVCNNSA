# author: Ajwahir
# Engineering Design Department
# IIT Madras
# email: ajwahir@gmail.com

# conversion of roof dataset to pointcloud

import numpy as np 
from open3d import *
import os
import pandas as pd


df = pd.read_csv("/home/raman/LFD/final_roof.csv")
labels = df.iloc[:, 1]
data = df.iloc[:, 2]
savepath = "/home/raman/Classification/VImages"

ii = 0

for data_no, v in enumerate(data):
	xyzs = v.replace(',',' ').split(' ')
	xyzs = np.array(xyzs, dtype=np.float)
	x, y, z = list(xyzs[::3]), list(xyzs[1::3]), list(xyzs[2::3])
	if len(x) == len(y) and len(y) == len(z):
		xyz = np.zeros((len(x),3))
		mid_x = (min(x)+max(x))/2
		mid_y = (min(y)+max(y))/2
		xyz[:,0] = x
		xyz[:,0] = xyz[:,0] - mid_x
		xyz[:,1] = y
		xyz[:,1] = xyz[:,1] - mid_y
		xyz[:,2] = z
# 
		pcd = PointCloud()
		pcd.points = Vector3dVector(xyz)
		if(labels[ii]==0):
			write_point_cloud(savepath+'/0/'+str(ii)+'.ply', pcd)
		if(labels[ii]==1):
			write_point_cloud(savepath+'/1/'+str(ii)+'.ply', pcd)
		if(labels[ii]==2):
			write_point_cloud(savepath+'/2/'+str(ii)+'.ply', pcd)
	ii = ii+1





