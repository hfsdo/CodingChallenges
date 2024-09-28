import sys
import os

#define global line counter
counter = 0

#read lines of file out of current working directory
def readFile(filename):
    folder = os.getcwd()
    f = open(folder+"\\"+filename, "r")
    return f.readlines()
    
#read lines out of stdIn
def readStdIn():
    return sys.stdin

#create counterstring
def getCounterStr(line, numbering):
    global counter
    if numbering == "-n":
        counter+=1
        return str(counter) + "\t"
    elif numbering == "-b":
        if line.strip() != "":
            counter+=1
            return str(counter) + "\t"
    return ''

#print lines
def printLines(lines, numbering):
    for line in lines:
        counterStr = getCounterStr(line, numbering)
        print(f'{counterStr}{line.strip()}')        

#define default values
numbering = "-"
stdIn = False
fromIndex = 1

#determine arguments(numbering [Y/N]) and source (stdIn or file)
if len(sys.argv) > 1:
    if sys.argv[1] in ["-n","-b"]:
        numbering = sys.argv[1]
        fromIndex = 2
        if len(sys.argv) == 2:
            stdIn = True
    elif sys.argv[1] == "-":
        stdIn = True
else:
    stdIn = True
    
#read source
if stdIn:
    printLines(readStdIn(), numbering)
else:
    for i in range(fromIndex, len(sys.argv)):
        filename = sys.argv[i]
        printLines(readFile(filename), numbering)
    

