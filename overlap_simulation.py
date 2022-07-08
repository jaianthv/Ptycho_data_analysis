import numpy as np
import math
import matplotlib.pyplot as plt
import cv2 as cv
import os




def get_center_points(step):
    start_position = (250,250)
    coordinates = []
    for i in range(250,2250,step):
        for j in range(250,2250,step):
            #print (i,j)
            coordinates.append([i,j])

    return coordinates
    
    

def create_circle(coordinate, R):
    blankimage = np.zeros((2500,2500), dtype=np.uint8)
    cv.circle(blankimage, center=coordinate, radius=R, color=(1,0,0), thickness=-1)
    return blankimage


def create_overlap_images(first_image, coordinates,radius):
    for i in range(len(coordinates)):
        multiply_image = create_circle((coordinates[i][0],coordinates[i][1]),radius)
        first_image = first_image + multiply_image
    return first_image
        


x = np.zeros((2500,2500))
coor = get_center_points(30)
final = create_overlap_images(x,coor,30)
os.chdir("C:/Ptycho/overlap_sim/")
cv.imwrite("focus_30nm_30nmSS.tif",final)

#for i in range(len(coor)):
#    x[coor[i][0]][coor[i][1]] = 1


plt.matshow(final)
plt.show()
