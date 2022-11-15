'''
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. You may take either 0 or 1 of each item.
Function Signature:
func knapsack(items: [Int: Int], limit: Int) -> Int
Target runtime and space complexity:
Time: O(nk), where n is the number of items and k is the limit
Space: O(nk)
Examples:
{1: 4, 2: 5, 3: 6, 5: 10}, 5 => 11
{1: 4, 2: 5, 3: 6, 5: 10}, 6 => 15

keep track of total weight
check each index
if total weight goes overweight, exclude
if the index is underweight, check max both including and excluding
include = helper(capacity - item_weight, limit, total_value + item_value)
exclude = helper(capacity, limit, total_value)

'''

def knapsack(items, limit):
    weights = []
    values = []
    for k, v in items.items():
        weights.append(k)
        values.append(v)

    return helper(weights, values, limit, 0, 0, {})

def helper(weights, values, limit, capacity, idx, memo):
    if (idx, capacity) in memo:
        return memo[(idx, capacity)]

    if idx >= len(weights) or capacity > limit:
        return 0

    include = 0
    if capacity + weights[idx] <= limit:
        include = values[idx] + helper(weights, values, limit, capacity + weights[idx], idx + 1, memo)

    exclude = helper(weights, values, limit, capacity, idx + 1, memo)

    memo[(idx, capacity)] = max(include, exclude)

    return memo[(idx, capacity)]

print(knapsack({1: 4, 2: 5, 3: 6, 5: 10}, 6), '15')
