"""
Date: 2020-10-05 Mon.
LeetCode: 304/Medium/DP
Difficulty: Easy

Problem Statement
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

Complexity
Time: O(mn) (m: # of rows, n: # of cols)
Space: O(mn) for mem matrix.
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Trivial cases
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.matrix = None
            return None
        self.matrix = matrix
        
        # Make a cumulative area sum memory matrix with zero-padding
        # at the beginning of rows and columns.
        self.mem = [[0 for j in range(len(self.matrix[0]) + 1)] for i in range(len(self.matrix) + 1)]
        
        # Fill in the memory.
        # The rule is
        # myself + cumulative above + cumulative left - double added area.
        for i in range(1, len(self.matrix) + 1):
            for j in range(1, len(self.matrix[0]) + 1):
                self.mem[i][j] = self.mem[i][j - 1] + self.mem[i - 1][j] + self.matrix[i - 1][j - 1] - self.mem[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Trivial case
        if not self.matrix: return 0
        
        # The rule is
        # Cumulative sum - upper margin - left margin + double subtracted area.
        return self.mem[row2 + 1][col2 + 1] - self.mem[row1][col2 + 1] - self.mem[row2 + 1][col1] + self.mem[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix_RowCache:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rowmem = [[0 for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            csum = 0
            for j in range(len(self.matrix[0])):
                csum += self.matrix[i][j]
                self.rowmem[i][j] = csum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        csum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                csum += self.rowmem[i][col2]
            else:
                csum += self.rowmem[i][col2] - self.rowmem[i][col1 - 1]
        return csum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
