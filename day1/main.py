import sys

if __name__ == "__main__":
    
    def readFile():
        f = open("/home/taymazturkmen/aoc2021/day1/input.txt", "r")
        data = f.read().splitlines()
        data = [ int(x) for x in data ]
        return data
    
    def p1():
        data = readFile()
        prevDepth = 0
        count = 0
        for i in data:
            if(prevDepth == 0):
                prevDepth = i
            elif(prevDepth<i):
                count=count+1
            prevDepth=i
        return count

    def p2():
        data = readFile()
        count = 0
        for i in range(len(data)-3):
            firstWindow = data[i] +data[i+1] + data[i+2]
            secondWindows = data[i+1] +data[i+2] + data[i+3]
            if(secondWindows>firstWindow):
                count = count+1
        return count
