from numpy import sqrt, newaxis
from numpy.random import randn

aa = randn(3, 100)

bb = aa / sqrt((aa * aa).sum(0)).[newaxis, :]

"""
2020-06-08 여기부터 하기
"""
print(min(bb), max(bb))