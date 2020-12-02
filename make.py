numberFiles = int(input())
dependencyGraph = dict()
for i in range(0, numberFiles):
    data = input().split(':')
    file = data[0]
    dependencies = data[1].strip().split(' ')

    if '' in dependencies:
        dependencies.remove('')

    if file not in dependencyGraph:
        dependencyGraph[file] = set()

    for dependency in dependencies:
        if dependency not in dependencyGraph:
            dependencyGraph[dependency] = set()
        
        dependencyGraph[dependency].add(file)

def dfs(file, visted, order):
    visted.add(file)
    for dependency in dependencyGraph[file]:
        if dependency not in visted:
            dfs(dependency, visted, order)

    order.insert(0, file)

fileChanged = input()

if fileChanged not in dependencyGraph:
    dependencyGraph[fileChanged] = set()

visted = set()
order = []
dfs(fileChanged, visted, order)

for file in order:
    print(file)
