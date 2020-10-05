# Coin Change
One of the newbie killer. I couldn't understand the optimal DP solution a few days ago but solving the problem with pen and paper gave me the insight.

## Problem Statement
Given a target price `price` and a list of units of coin `coins`, find the number of ways to form the `price` using given types of `coins`. Assume we can use infinite amount of each coins in `coins`.

## Algorithm - Basic
We will draw a table (counting indices from 0) to find a trend. Each column represents the target price. Each row represents the usable units of coins. Assume;
```price = 0, 1, 2, ... , 10`, `coins = [1, 2, 5]```
Then the columns will be 0, 1, 2, ..., 10 and the rows will be [1], [1, 2], [1, 2, 5].


![step1](/HackerRank/DP/CoinChange/step1.png?raw=true "Step 1")
Row 0 is easy; using only 1-coin, there are only one way to form a target price, no matter how much it is. Thus,  
```table[0][jj] = 1 for jj in [1, 2, ... , 10]```


![step2](/HackerRank/DP/CoinChange/step2.png?raw=true "Step 2")
Row 1 is the same as the first row until column 1. At column 2, there is a way to form price 2 other than the combination we discussed in the previous step; using one 2-coin and no 1-coin. Thus,  
```table[1][2] = 2```


![step3](/HackerRank/DP/CoinChange/step3.png?raw=true "Step 3")
Let's analyze how this value is comprised of. It can be interpreted as 'making price 2 using 1-coins' + 'making price 2 using 1-coins and one 2-coin'. The latter is equivalent to 'making price 2-2 = 0 using 1-coins'. Thus, the value is summation of the value right above and the value on the cell twice away from here;  
```table[1][2] = table[0][2] + table[1][2 - 2]```


![step4](/HackerRank/DP/CoinChange/step4.png?raw=true "Step 4")
We can continue this calculation in this row;
```
table[1][3] = table[0][3] + table[1][3 - 2],
table[1][4] = table[0][4] + table[1][4 - 2], ...
```


![step5](/HackerRank/DP/CoinChange/step5.png?raw=true "Step 5")
Row 1 is filled. Let's go to row 2.


![step6](/HackerRank/DP/CoinChange/step6.png?raw=true "Step 6")
Row 2 is the same with the previous row until column 4; right before meeting the price that is same as the newly added coin.


![step7](/HackerRank/DP/CoinChange/step7.png?raw=true "Step 7")
At column 5, we can form price 5 by either using the same combination as the previous row, or using only single 5-coin. The latter is the same as 'making price 5-5 = 0 using 1-coins and 2-coins'. Each way can be represented as `table[1][5]` and `table[2][0]`, so we can write the current value as follows;
```table[2][5] = table[1][5] + table[2][5 - 5]```


![step8](/HackerRank/DP/CoinChange/step8.png?raw=true "Step 8")
Now fill the rest of the row with the same rule.
```
table[2][6] = table[1][6] + table[2][6 - 5],
table[2][7] = table[1][7] + table[2][7 - 5], ...
```

Now, write the corresponding code.
```python
def getWays2d(price, coins):
    table = [[1] + [0] * price for ii in range(len(coins))]
    for jj in range(1, price + 1):
        table[0][jj] = 1
    for ii in range(1, len(coins)):
        for jj in range(coins[ii]):
            table[ii][jj] = table[ii - 1][jj]
        for jj in range(coins[ii], price + 1):
            table[ii][jj] = table[ii - 1][jj] + table[ii][jj - coins[ii]]
    return table[-1][-1]
```

## Algorithm - Optimal
Actually, we only need the last row of the `table` above. Also, since the beginning of each row is the same as previous row, we can make a single row list and reuse it over and over.  
The following can be omitted when using 1D list;
```table[ii][jj] = table[ii - 1][jj]```
The following can be simplified when using 1D list by deleting the row dimension;
```
table[ii][jj] = table[ii - 1][jj] + table[ii][jj - coins[ii]]
↓
table[jj] = table[jj] + table[jj - coins[ii]]
```
With this recurrence formula, we can use `for cc in coins` and put `cc` instead of `coins[ii]`. The following is the optimized code;
```python
def getWays_optimal(price, coins):
    dp = [1] + [0] * price
    for cc in coins:
        for jj in range(cc, price + 1):
            dp[jj] = dp[jj] + dp[jj - cc]
        print(dp)
    return dp[-1]
```
