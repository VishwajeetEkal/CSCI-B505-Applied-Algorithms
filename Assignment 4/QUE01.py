def MinimumExpenditure(AppleTreePrice):
    n = len(AppleTreePrice)

    for k in range(1, n):
        for i in range(3):
            min_cost = min(AppleTreePrice[k-1][(j % 3)] for j in range(3) if j != i)
            AppleTreePrice[k][i] += min_cost

    return min(AppleTreePrice[-1])

print(MinimumExpenditure([[1,2,3],[1,2,3],[1,2,3]]))
print(MinimumExpenditure([[4,12,7],[2,34,13]]))