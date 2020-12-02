data = input().split(' ')
numberCups = int(data[0])
cups = [int(number) for number in data[1:-1]] 
target = int(data[-1])

initialState = [0 for cup in cups]
initialState[0] = cups[0]
states = []
states.append(initialState)

def dfs(state, sum, visted):
    visted.append(state)
    for cup in state:
        if cup > 0:
            for 
    return sum
# dependencyGraph = dict()
# for i in range(0, numberFiles):
#     data = input().split(':')
#     file = data[0]
#     dependencies = data[1].strip().split(' ')

#     if '' in dependencies:
#         dependencies.remove('')

#     if file not in dependencyGraph:
#         dependencyGraph[file] = set()

#     for dependency in dependencies:
#         if dependency not in dependencyGraph:
#             dependencyGraph[dependency] = set()
        
#         dependencyGraph[dependency].add(file)

# def dfs(file, visted, order):
#     visted.add(file)
#     for dependency in dependencyGraph[file]:
#         if dependency not in visted:
#             dfs(dependency, visted, order)

#     order.insert(0, file)

# fileChanged = input()

# if fileChanged not in dependencyGraph:
#     dependencyGraph[fileChanged] = set()

# visted = set()
# order = []
# dfs(fileChanged, visted, order)

# for file in order:
#     print(file)




# 2 5 2 3