from AOC import *

MaxRedCubes = 12
MaxGreenCubes = 13
MaxBlueCubes = 14

IsPowerCalc = True

def parseLine(line: str):
    game = line.split(": ")
    id = int(game[0].split("Game ")[1])

    cubes = game[1].split("; ")

    if not IsPowerCalc:
        for cube in cubes:
            if parseGame(cube.split(", ")):
                return 0
            
        return id

    lowest = findLowestCubeCount(cubes)
    
    return lowest[0] * lowest[1] * lowest[2]
            

def parseGame(cubes):
    redCubes = greenCubes = blueCubes = 0
    for cube in cubes:
        if "red" in cube:
            redCubes = int(cube.split(" red")[0])
        if "green" in cube:
            greenCubes = int(cube.split(" green")[0])
        if "blue" in cube:
            blueCubes = int(cube.split(" blue")[0])
    return redCubes > MaxRedCubes or greenCubes > MaxGreenCubes or blueCubes > MaxBlueCubes


def findLowestCubeCount(cubes):
    lowestRedCubes = lowestGreenCubes = lowestBlueCubes = 0
    for cubes0 in cubes:
        for cube in cubes0.split(", "):
            if "red" in cube:
                redCubes = int(cube.split(" red")[0])
                if redCubes > lowestRedCubes:
                    lowestRedCubes = redCubes
            if "green" in cube:
                greenCubes = int(cube.split(" green")[0])
                if greenCubes > lowestGreenCubes:
                    lowestGreenCubes = greenCubes
            if "blue" in cube:
                blueCubes = int(cube.split(" blue")[0])
                if blueCubes > lowestBlueCubes:
                    lowestBlueCubes = blueCubes
    return [ lowestRedCubes, lowestGreenCubes, lowestBlueCubes ]
    


lines = readFile("input.txt")

value = 0

for line in lines:
    value = value + parseLine(line)

print(value)