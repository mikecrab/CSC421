testCases = int(input())
for i in range(0, testCases):
    customerAmount = int(input())

    customers = []
    for i in range(0, customerAmount):
        woodData = input()
        woodData = woodData.split()
        time = 0
        for i in range(1, len(woodData)): 
            time += int(woodData[i])
        customers.append(time)

    customers.sort()
    totalTime = 0
    for i in customers:
        totalTime += totalTime + i
    
    averageTime = totalTime / customerAmount

    print(averageTime)
