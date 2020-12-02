numberRoutes = int(input())
routeGraph = dict()
for i in range(0, numberRoutes):
    route = input().split()

    station = route[0]
    if station not in routeGraph:
        routeGraph[station] = set()
    connections = route[1:]

    for connection in connections:
        if connection not in routeGraph:
            routeGraph[connection] = set()
        
        routeGraph[station].add(connection)
        routeGraph[connection].add(station)

def dfs(station, end, visted, route):
    visted.add(station)
    route.append(station)
    if station == end:
        return route
    
    for connection in routeGraph[station]:
        if connection not in visted:
            route = dfs(connection, end, visted, route)
            if route[-1] == end:
                return route

    route.pop()
    return route

path = input().split()

start = path[0]
end = path[1]
if start not in routeGraph:
    routeGraph[start] = set()
if end not in routeGraph:
    routeGraph[end] = set()
visted = set()
route = []

route = dfs(start, end, visted, route)
if route:
    route = ' '.join([str(elem) for elem in route])
else:
    route = 'no route found'
print(route)