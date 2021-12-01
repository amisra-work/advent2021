def readInputFile(filename):
    l = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = int(line.rstrip())
            l.append(line)
    return l
