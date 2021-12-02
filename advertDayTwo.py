from common_code import readInputFilePairs

def partOne(arr):
    depth = 0 
    latitude = 0
    for correction in arr:
        if correction[0] == 'forward':
            latitude += correction[1]
        elif correction[0] == 'down':
            depth += correction[1]
        elif correction[0] == 'up':
            depth -= correction[1]
    return (depth, latitude)

def partTwo(arr):
    depth = 0 
    latitude = 0
    aim = 0 
    for correction in arr:
        if correction[0] == 'forward':
            latitude += correction[1]
            depth += (aim * correction[1])
        elif correction[0] == 'down':
            aim += correction[1]
        elif correction[0] == 'up':
            aim -= correction[1]
    return (depth, latitude)


def helper(arr):
    l = []
    for elem in arr:
        l.append([elem[0],int(elem[1])])
    return l

if __name__ == "__main__":
    filename = 'advertDayTwoInput.txt'
    l = helper(readInputFilePairs(filename))
    a = partOne(l)
    print(a[0] * a[1])
    s = helper(readInputFilePairs(filename))
    b = partTwo(s)
    print(b[0] * b[1])