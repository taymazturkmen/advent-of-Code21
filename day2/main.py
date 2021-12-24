import sys

if __name__ == "__main__":

    def readFile():
        f = open("/home/taymazturkmen/aoc2021/day2/input.txt", "r")
        data = f.read().splitlines()
        return data

    def p1():
        x = 0
        y = 0
        data = readFile()
        for i in data:
            splittedData = i.split(" ")
            if splittedData[0] == "forward":
                x = x + int(splittedData[1])
            if splittedData[0] == "up":
                y = y - int(splittedData[1])
            if(splittedData[0] == "down"):
                y = y + int(splittedData[1])
        return x*y

    def p2():
        aim = 0
        x = 0
        y = 0
        data = readFile()
        for i in data:
            splittedData = i.split(" ")
            if splittedData[0] == "forward":
                x = x + int(splittedData[1])
                y = y + aim * int(splittedData[1])
            if splittedData[0] == "up":
                aim = aim - int(splittedData[1])
            if(splittedData[0] == "down"):
                aim = aim + int(splittedData[1])
        return x*y
