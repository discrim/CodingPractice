"""
Date: 2020-10-05 Mon.
LeetCode: 361/Medium/DP

Problem Statement
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Complexity
Time: O(mn) (m: # of rows, n: # of cols)
    There are 4 nested loops. Each loop takes O(mn) time.
Space: O(mn)
    Need memory with equivalent size to the grid.
"""

def maxKilledEnemies(grid):
    if len(grid) == 0: return 0
    
    # Memoize how many Es a bomb can kill when placed at each 0s
    dp = [[0 for jj in range(len(grid[0]))] for ii in range(len(grid))]
    max_kills = 0
    
    # Scan from left to right and record the row kills.
    # Each value in dp after this loop is the killcount
    # only counting the enemies on the left from the placement.
    for ii in range(len(grid)):
        row_kills = 0
        for jj in range(len(grid[0])):
            if grid[ii][jj] == 'E':
                row_kills += 1
            elif grid[ii][jj] == 'W':
                row_kills = 0
            else:
                dp[ii][jj] = row_kills
    
    # Scan from right to left and record the row kills
    # Each value in dp after this loop is the killcount
    # with complete row kills.
    for ii in range(len(grid)):
        row_kills = 0
        for jj in range(len(grid[0]) - 1, -1, -1):
            if grid[ii][jj] == 'E':
                row_kills += 1
            elif grid[ii][jj] == 'W':
                row_kills = 0
            else:
                dp[ii][jj] += row_kills
    
    # Scan from up to down and record the col kills.
    # Each value in dp after this loop is the killcount
    # with complete row kills and partial col kills 
    # only counting the enemies on the above from the placement.
    for jj in range(len(grid[0])):
        col_kills = 0
        for ii in range(len(grid)):
            if grid[ii][jj] == 'E':
                col_kills += 1
            elif grid[ii][jj] == 'W':
                col_kills = 0
            else:
                dp[ii][jj] += col_kills
    
    # Scan from down to up and record the col kills.
    # Each value in dp after this loop is the killcount
    # with complete row kills and complete col kills.
    for jj in range(len(grid[0])):
        col_kills = 0
        for ii in range(len(grid) - 1, -1, -1):
            if grid[ii][jj] == 'E':
                col_kills += 1
            elif grid[ii][jj] == 'W':
                col_kills = 0
            else:
                dp[ii][jj] += col_kills
                max_kills = max(max_kills, dp[ii][jj])
    
    return max_kills


if __name__ == '__main__':
    ins = [[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]]
    for inp in ins:
        print(maxKilledEnemies(inp))
    