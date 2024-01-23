def knapsack_01(values, weights, capacity):
    n = len(values)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    max_value = dp[n][capacity]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return max_value, selected_items[::-1]


n = int(input("Enter the number of items: "))
values = list(map(int, input("Enter the values of the items (space-separated): ").split()))
weights = list(map(int, input("Enter the weights of the items (space-separated): ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))


max_value, selected_items = knapsack_01(values, weights, capacity)


print(f"Maximum value: {max_value}")
print("Selected items:", selected_items)
