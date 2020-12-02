def batmanacci(string_number, character_index):
    if string_number == 1:
        return "N"
    elif string_number == 2:
        return "A"

    else:
        while string_number > 2:
            if character_index > fibNumbers[string_number - 2]:
                character_index -= fibNumbers[string_number - 2]
                string_number -= 1
            else:
                string_number -= 2
            return batmanacci(string_number, character_index)


data = input()
data = data.split()
stringNumber = int(data[0])
characterIndex = int(data[1])

fibNumbers = dict()
fibNumbers[1] = 1
fibNumbers[2] = 1
for i in range(3, stringNumber+1):
    fibNumbers[i] = (fibNumbers[i-1] + fibNumbers[i-2])

letter = batmanacci(stringNumber, characterIndex)
print(letter)
