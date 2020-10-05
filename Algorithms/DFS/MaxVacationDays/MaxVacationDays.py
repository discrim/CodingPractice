"""
Date: 2020-10-05 Mon.
LeetCode: 568/Hard/DP
Difficulty: Hard

Problem Statement
    LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

    Rules and restrictions:
    You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
    The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
    You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.
    For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
    You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.

    Example 1:
    Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
    Output: 12
    Explanation: 
    Ans = 6 + 3 + 3 = 12. 

    One of the best strategies is:
    1st week : fly from city 0 to city 1 on Monday, and play 6 days and work 1 day. 
    (Although you start at city 0, we could also fly to and start at other cities since it is Monday.) 
    2nd week : fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
    3rd week : stay at city 2, and play 3 days and work 4 days.
    Example 2:
    Input:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
    Output: 3
    Explanation: 
    Ans = 1 + 1 + 1 = 3. 

    Since there is no flights enable you to move to another city, you have to stay at city 0 for the whole 3 weeks. 
    For each week, you only have one day to play and six days to work. 
    So the maximum number of vacation days is 3.
    Example 3:
    Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
    Output: 21
    Explanation:
    Ans = 7 + 7 + 7 = 21

    One of the best strategies is:
    1st week : stay at city 0, and play 7 days. 
    2nd week : fly from city 0 to city 1 on Monday, and play 7 days.
    3rd week : fly from city 1 to city 2 on Monday, and play 7 days.
    Note:
    N and K are positive integers, which are in the range of [1, 100].
    In the matrix flights, all the values are integers in the range of [0, 1].
    In the matrix days, all the values are integers in the range [0, 7].
    You could stay at a city beyond the number of vacation days, but you should work on the extra days, which won't be counted as vacation days.
    If you fly from the city A to the city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
    We don't consider the impact of flight hours towards the calculation of vacation days.

Complexity
Time: O(n^2 * k). (n: # of cities, k: # of weeks)
    memo array of size n * k is filled and each cell filling takes O(n) time because of the for loop.
Space: O(n * k).
    Size of memo array.
"""

class Solution:
    def maxVacationDays(self, flights, days):
        # Memoization array.
        # Each cell represents the maximum vacation days
        # when starting in ith row (city)
        # and starting at jth col (week).
        memo = [[-1 for jj in range(len(days[0]))] for ii in range(len(days))]
        return self.dfs(memo, flights, days, 0, 0)
    
    def dfs(self, memo, flights, days, curcity, weeknum):
        if weeknum == len(days[0]):
            return 0
        
        if memo[curcity][weeknum] != -1:
            return memo[curcity][weeknum]
        
        maxvac = 0
        for tocity in range(len(flights)):
            if curcity == tocity or flights[curcity][tocity] == 1:
                vac = days[tocity][weeknum] + self.dfs(memo, flights, days, tocity, weeknum + 1)
                maxvac = max(maxvac, vac)
        memo[curcity][weeknum] = maxvac
        for row in memo:
            print(row)
        print('\n')
        return maxvac

class Solution_naive: # Time limit exceeded
    def maxVacationDays(self, flights, days):
        return self.dfs(flights, days, 0, 0)
    
    def dfs(self, flights, days, curcity, weeknum):
        if weeknum == len(days[0]): return 0
        
        maxvac = 0
        for tocity in range(len(flights)):
            if curcity == tocity or flights[curcity][tocity] == 1:
                vac = days[tocity][weeknum] + self.dfs(flights, days, tocity, weeknum + 1)
                maxvac = max(maxvac, vac)
        return maxvac