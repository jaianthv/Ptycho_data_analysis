import os
import cv2 as cv
import numpy as np


#folder = "C:/Ptycho/Resolution_enhancement/"
#folder = "C:/Ptycho/Ptychography_paper/Nanorod_XMCD/AMP_1/"
#folder = "C:/Ptycho/paper_v5/images/defocus_blurr/"
folder = "C:/Ptycho/paper_v5/images/sharpness/"
os.chdir(folder)
file  ="Pic3_92.png"
image = cv.imread(file,-1)
image = cv.resize(image, (512,512), interpolation = cv.INTER_AREA)
image = np.array(image, dtype=np.float64)
blurr = cv.Laplacian(image, cv.CV_64F).var()
print (blurr)





##### blur data #####


# Nanorods            Amp_105.tif        0.00010060874394377018
# BN nanorods         Res_enhance        41.204345703125
# CN nanotubes        Res_enhance        62.41839871596312


###### blurr data vs focus - defocu

# CNT data
# 62 nm               focus62.png        71.21681785583496
# 500 nm              defocus500.png     61.290361404418945
# 1000 nm             defocus1000.png    62.15309143066406


###### blur STXM CNT and Ptycho CNT
# STXM                STXM_CNT.png       140.70319686247967
# PTYCHO              PTYCHO_CNT.png     173.04928217747363
