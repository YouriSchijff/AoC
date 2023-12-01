from AOC import *

IncludeSpelledNumbers = True

def replaceSpelled(line):
    newLine = line

    # We need to add the replaced words too because of instances like this
    # eightwo
    # nineighthree
    newLine = newLine.replace("one",   "one1one")
    newLine = newLine.replace("two",   "two2two")
    newLine = newLine.replace("three", "three3three")
    newLine = newLine.replace("four",  "four4four")
    newLine = newLine.replace("five",  "five5five")
    newLine = newLine.replace("six",   "six6six")
    newLine = newLine.replace("seven", "seven7seven")
    newLine = newLine.replace("eight", "eight8eight")
    newLine = newLine.replace("nine",  "nine9nine")

    print(line)
    print(newLine)

    return newLine


def getNumbersFromLine(line):
    characters = list(line)
    
    if IncludeSpelledNumbers:
        characters = list(replaceSpelled(line))

    numbers = []

    for character in characters:
        try:
            numbers.append(int(character))
            break
        except:
            continue

    for character in reversed(characters):
        try:
            numbers.append(int(character))
            break
        except:
            continue


    if numbers:
        return numbers
    return None


def parseNumbers(numbers):
    return int(''.join(map(str, numbers)))


lines = readFile("1.txt")

value = 0

for line in lines:
    numbers = getNumbersFromLine(line)

    print(numbers)

    if numbers == None:
        continue

    print(parseNumbers(numbers))

    value = value + parseNumbers(numbers)

print(value)