def numberOfWays(amount, coinValues):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coinValues:
        for x in range(coin, amount + 1):
            dp[x] += dp[x-coin]
    return dp[-1]


print(numberOfWays(5, [1, 2, 5]) == 4) 
print(numberOfWays(2, [1, 2, 3]) == 2)
print(numberOfWays(10, [2, 5, 3, 6]) == 5)
print(numberOfWays(4, [5]) == 0)
