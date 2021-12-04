from common_code import readInputFileNumbersString
from collections import Counter

def partOne(arr):
    g = ''
    e = ''
    lengthNumber = len(arr[0])
    lengthArr = len(arr)
    for i in range(lengthNumber):
        one, zero = 0,0
        for j in range(lengthArr):
            if arr[j][i] == '0':
                zero += 1
            elif arr[j][i] == '1':
                one += 1
        if zero > one:
            g = g + '0'
            e = e + '1'
        elif one > zero:
            g = g + '1'
            e = e + '0'
    return (int(g,2)*int(e,2))
    

def partTwo(arr, filename):
    arr = [elem for elem in open(filename).read().strip().split('\n')]
    oxygenGeneratorRating = ''
    scrubberRating = ''
    for i in range(len(arr[0])):
        common = Counter([elem[i] for elem in arr])

        if common['0'] > common['1']:
            arr = [elem for elem in arr if elem[i] == '0']
        else:
            arr = [elem for elem in arr if elem[i] == '1']
        oxygenGeneratorRating = arr[0]

    arr = [elem for elem in open(filename).read().strip().split('\n')]
    for i in range(len(arr[0])):
        common = Counter([elem[i] for elem in arr])
        if common['0'] > common['1']:
            arr = [elem for elem in arr if elem[i] == '1']
        else:
            arr = [elem for elem in arr if elem[i] == '0']
        if arr:
            scrubberRating = arr[0]
    return (int(oxygenGeneratorRating,2)*int(scrubberRating,2))


if __name__ == "__main__":
    filename = 'inputs/advertDayThreeInput.txt'
    l = readInputFileNumbersString(filename)
    a = partOne(l)
    print("Power Consumption: %d" % a)
    s = readInputFileNumbersString(filename)
    b = partTwo(s, filename)
    print("Life Support rating: %d" %b)
