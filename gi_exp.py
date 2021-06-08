# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:21:02 2021

@author: Pavel Gostev
"""
import matplotlib.pyplot as plt
from gi.experiment import ImgAnalyser, ImgViewer

"""
settings_file -- путь к файлу с настройками эксперимента в формате json
"""
settings_file = settings_file = r'H:\Downloads\17_04_2019_obj_v\17_04_2019_obj_v.txt'


analyser = ImgAnalyser(settings_file)
analyser.calculate_all()
# analyser.calculate_ghostimage()
# analyser.calculate_contrast()
# analyser.calculate_xycorr()
# analyser.calculate_timecorr()
print(analyser.information)

viewer = ImgViewer(analyser.ghost_data)
viewer.accumulate(analyser.contrast_data)
viewer.accumulate(analyser.xycorr_data)
viewer.accumulate(analyser.ref_data[0])
viewer.show(1)

plt.plot(analyser.times, analyser.timecorr_data)
plt.show()
