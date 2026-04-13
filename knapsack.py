def knapsack(weights, values, W):
    n = len(weights)
    
    prev = [0]*(W+1)
    
    # Base case
    for w in range(weights[0], W+1):
        prev[w] = values[0]
    
    for i in range(1, n):
        for w in range(W, -1, -1):  # IMPORTANT: reverse
            not_take = prev[w]
            
            take = 0
            if weights[i] <= w:
                take = values[i] + prev[w - weights[i]]
            
            prev[w] = max(take, not_take)
    
    return prev[W]