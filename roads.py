testCases = []
while(True):
    data = input()

    if data == '':
        break
    data = data.split(' ')
    roadGraph = dict()
    reverseGraph = dict()

    numberLocations = int(data[0])
    numberRoads = int(data[1])


    for i in range(0, numberLocations):
        roadGraph[i] = set()
        reverseGraph[i] = set()
    
    for i in range(0, numberRoads):
        roadData = input().split(' ')

        road0 = int(roadData[0])
        road1 = int(roadData[1])

        roadGraph[road0].add(road1)
        reverseGraph[road1].add(road0)
    
    testCases.append(dict(graph=roadGraph, reverseGraph=reverseGraph))

def dfs(location, visited, graph, postOrder = None):
    visited[location] = True

    for connectedLocation in graph[location]:
        if visited[connectedLocation] == False:
            dfs(connectedLocation, visited, graph, postOrder)

    if postOrder != None:
        postOrder.append(location)

def canBeFixed(graph, sink, source):
    sinks = 0
    sources = 0
    roadsToSink = 0

    for location in graph:
        isSink = False
        if len(graph[location]) == 0:
            sinks += 1
            isSink = True

        isSource = True
        for otherLocation in graph:
            if location in graph[otherLocation]:
                isSource = False
                if isSink:
                    roadsToSink += 1
        if isSource:
            sources += 1

    if sources == 1 and sinks == 1 and sink in graph[source] and roadsToSink > 1:
        return True


for i in range(len(testCases)):
    testCase = testCases[i]
    visited = dict()
    for key in testCase['graph']:
        visited[key] = False
    postOrder = []
    
    for location in visited:
        if visited[location] == False:
            dfs(location, visited, testCase['graph'], postOrder)

    visited = dict()
    for key in testCase['graph']:
        visited[key] = False
    
    counter = 0
    firstPost = postOrder[0]
    lastPost = postOrder[-1]
    while(len(postOrder) > 0):
        location = postOrder.pop()
        if visited[location] == False:
            counter += 1
            dfs(location, visited, testCase['reverseGraph'])
    
    returnString = "Case " + str(i + 1) + ": "
    if counter == 1:
        returnString += "valid"
    else:
        if canBeFixed(testCase['graph'], firstPost, lastPost):
            returnString += str(lastPost) + " " + str(firstPost)
        else:
            returnString += "invalid"
    print(returnString)