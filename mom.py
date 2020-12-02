numberFlights = int(input())
flightGraph = dict()
for i in range(0, numberFlights):
    data = input()
    data = data.split()
    if(data[0] not in flightGraph):
        flightGraph[data[0]] = []
    
    if(data[1] not in flightGraph):
        flightGraph[data[1]] = []

    flightGraph[data[0]].append(data[1])

cities = []
while(True):
    city = input()
    if(city == ''):
        break
    cities.append(city)
    if city not in flightGraph:
        flightGraph[city] = []

def cityDFS(city, visted, stack):
    visted[city] = True
    stack[city] = True
    
    for destination in flightGraph[city]:
        if visted[destination] == False:
            if cityDFS(destination, visted, stack) == True:
                return True
        elif stack[destination] == True:
            return True

    stack[city] = False
    return False



def isCitySafe(city):
    visted = dict()
    stack = dict()
    for key in flightGraph:
        visted[key] = False
        stack[key] = False
    safe = cityDFS(city, visted, stack)
    if safe:
        return 'safe'
    else:
        return 'trapped'

for city in cities:
    safe = isCitySafe(city)
    print(city + ' ' + safe)

# 5
# Arlington San_Antonio
# San_Antonio Baltimore
# Baltimore New_York
# New_York Dallas
# Baltimore Arlington
# San_Antonio
# Baltimore
# New_York