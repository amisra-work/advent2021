def readInputFileNumbers(filename):
    l = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = int(line.rstrip())
            l.append(line)
    return l

def readInputFilePairs(filename):
    l = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line =line.rstrip().split(' ')
            l.append(line)
    return l

def readInputFileNumbersString(filename):
    l = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            l.append(str(line))
    return l