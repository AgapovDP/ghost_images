# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:12:24 2022

@author: von.gostev
""" 
import __init__
from gi import ImgEmulator
from lightprop2d import Beam2D, rectangle_hole, random_wave
import matplotlib.pyplot as plt

npoints = 512
wl0 = 0.632
nimg = 1000
area_size = 1000

test = ImgEmulator(area_size, npoints, wl0, nimg,
                   init_field_gen=random_wave,
                   init_gen_args=(4,),
                   object_gen=rectangle_hole,
                   object_gen_args=(500, 100),
                   parallel_njobs=2,
                   use_gpu=True
                   )
test.calculate_xycorr()

plt.plot(test.xycorr_data[test.npoints // 2])
plt.show()