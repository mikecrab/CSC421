numberRoutines = int(input())
minQuickChanges = float('Inf')
dances = []
for i in range(0, numberRoutines):
    dance = input()
    dances.append(dance)
def countQuickChanges(routine):
    num = 0
    for i in range(1, len(routine)):
        chars = set()
        for char in routine[i-1]:
            chars.add(char)

        for char in routine[i]:
            if char in chars:
                num += 1
    return num

def chooseDancers(remaining_dances, routine, dance_index):
    global minQuickChanges
    # print(routine)
    if len(remaining_dances) == 0:
        quickChanges = countQuickChanges(routine)
        if quickChanges < minQuickChanges:
            minQuickChanges = quickChanges
        return True
    for i in range(len(remaining_dances)):
        routine[dance_index] = remaining_dances[i]
        # remaining_dances.remove(dance)
        dance = remaining_dances[i]
        del remaining_dances[i]
        chooseDancers(remaining_dances, routine, dance_index + 1)
        remaining_dances.insert(i, dance)

chooseDancers(dances, ['' for i in range(numberRoutines)], 0)
print(minQuickChanges)
