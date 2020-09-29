# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 00:12:14 2020

@author: shiny
"""

def meanGroups(a):
    means = []
    for ii in range(len(a)):
        means.append(sum(a[ii]) / len(a[ii]))
    means = set(means)
    return means


if __name__ == "__main__":
    in1 = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]]
    print(meanGroups(in1))