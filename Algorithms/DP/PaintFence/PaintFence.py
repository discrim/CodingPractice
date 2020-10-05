"""
Date: 2020-10-05 Mon.
LeetCode: 276/Easy/DP
My Difficulty: Medium
Solution: https://leetcode.com/problems/paint-fence/discuss/178010/The-only-solution-you-need-to-read

Problem Statement
There is a fence with n posts, each post can be painted with one of the k colors. You have to paint all the posts such that no more than two adjacent fence posts have the same color. Return the total number of ways you can paint the fence.
Note:
n and k are non-negative integers.

Complexity
Time: O(n)
Space: O(n)
"""

def numWays(n: int, k: int) -> int:
	if n == 0: return 0
	elif n == 1: return k
	dp = []
	dp.append(k)
	dp.append(k * k)
	for ii in range(2, n):
		dp.append((dp[ii - 1] + dp[ii - 2]) * (k - 1))
	return dp[-1]


if __name__ == '__main__':
    ins = [[3, 2]]
    for inp in ins:
        print(numWays(inp[0], inp[1]))