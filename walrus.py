numberWeights = int(input())
weights = []
for i in range(0, numberWeights):
    weight = int(input())
    weights.append(weight)

memo = [[0 for i in range(sum(weights))] for j in range(numberWeights + 1)]
for i in range(sum(weights)):
    memo[numberWeights][i] = i
    memo[numberWeights + 1][i] = 0
for i in reversed(range(numberWeights)):
    for j in reversed(range(sum(weights) - 1)):
        if(j in weights):
            include = memo[i + 1][j + weights[i]]
            exclude = memo[i + 1][j]
            # print(weights[i])
            if 1000 - abs(include) <= 1000 - abs(exclude):
                memo[i][j] = include
            else:
                memo[i][j] = exclude

print(memo)