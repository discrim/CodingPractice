# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:23:00 2020

@author: shiny
"""

def gridChallenge(grid):
    role = len(grid)
    cole = len(grid[0])
    nums = [[0] * cole] * role
    for row in range(role):
        print('\nrow = ', row)
        for col in range(cole):
            print('%s is %d' % (grid[row][col], ord(grid[row][col])))
            nums[row][col] = ord(grid[row][col])
            print('nums[%d][%d] is %d' % (row, col, nums[row][col]))
            print(nums)

    print(nums)

    for row in nums:
        row.sort()
    
    for col in range(cole):
        for row in range(1, role):
            print('%d - %d' % (nums[row][col], nums[row - 1][col]))
            if nums[row][col] - nums[row - 1][col] < 0:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    '''
    3
    3
    abc
    lmp
    qrt
    3
    mpxz
    abcd
    wlmf
    4
    abc
    hjk
    mpq
    rtv
    '''
    in1 = ['abc', 'lmp', 'qrt']
    #print(gridChallenge(in1))
    nums = [[0] * 3] * 4
    print(nums)
    nums[0][1] = 3
    print(nums)