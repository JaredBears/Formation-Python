def maxProfitPotential(prices):
    maxProfit = 0
    minPrice = float('inf')

    for curPrice in prices:
        profit = curPrice - minPrice
        maxProfit = max(maxProfit, profit)
        minPrice = min(minPrice, curPrice)

    return maxProfit

print(maxProfitPotential([7,1,5,3,6,4]) == 5)
print(maxProfitPotential([7,6,4,3,1]) == 0)
print(maxProfitPotential([3,1,5]) == 4)
print(maxProfitPotential([1,2,3,5,6,7]) == 6)
print(maxProfitPotential([3,3,3,3,3,3]) == 0)
print(maxProfitPotential([0.55,1.23,3.53,1.75,5.16]) == 4.61)
print(maxProfitPotential([1,9]) == 8)
print(maxProfitPotential([8,2]) == 0)
print(maxProfitPotential([1]) == 0)
print(maxProfitPotential([]) == 0)
