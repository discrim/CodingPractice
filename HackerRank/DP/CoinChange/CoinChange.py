def getWays_optimal(price, coins):
    dp = [1] + [0] * price
    for cc in coins:
        for jj in range(cc, price + 1):
            dp[jj] = dp[jj] + dp[jj - cc]
        print(dp)
    return dp[-1]

def getWays_basic(price, coins):
    table = [[1] + [0] * price for ii in range(len(coins))]
    for jj in range(1, price + 1):
        table[0][jj] = 1
    for ii in range(1, len(coins)):
        for jj in range(coins[ii]):
            table[ii][jj] = table[ii - 1][jj]
        for jj in range(coins[ii], price + 1):
            table[ii][jj] = table[ii - 1][jj] + table[ii][jj - coins[ii]]
    return table[-1][-1]


if __name__ == '__main__':
    ins = []
    ins.append([5, [1, 2, 5]])
    for cur in ins:
        print(getWays_basic(cur[0], cur[1]))
        print(getWays_optimal(cur[0], cur[1]))