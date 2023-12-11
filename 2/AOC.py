def readFile(fileName: str):
    lines = "NULL"

    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    return lines