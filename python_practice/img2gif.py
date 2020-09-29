# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:37:56 2020

@author: junkeunp@umich.edu
"""
from os import listdir
from os.path import basename
from imageio import imread, mimsave

def main(dir):
    images = []
    allfiles = listdir(dir)
    pngfiles = [ff for ff in allfiles if ff.endswith('.png')]
    for filename in pngfiles:
        images.append(imread(dir + '/' + filename))
    kwargs = {"duration":1}
    try:
        resultname = '/' + basename(dir) + '.gif'
    except:
        resultname = '/movie.gif'
    mimsave(dir + resultname, images, **kwargs)

if __name__ == "__main__":
    mypath = r'D:\DevPath\MDP_2020_DELL\AngleCalculation\IQPhasorPlot\cycles\center (2) 301~303'
    main(mypath)