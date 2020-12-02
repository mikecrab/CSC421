data = input()
data = data.split()
numberCommercials = int(data[0])
commercialCost = int(data[1])

profit = [0 for i in range(0, numberCommercials)]
data = input()
numberViewers = data.split()

profit[0] = int(numberViewers[0]) - commercialCost
for i in range(1, numberCommercials):
    timeSlotProfit = int(numberViewers[i]) - commercialCost
    profit[i] = max(profit[i-1] + timeSlotProfit, timeSlotProfit)

print(max(profit))
