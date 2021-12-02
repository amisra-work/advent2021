from common_code import readInputFileNumbers

def partOne(arr): 
    deeper = 0
    depths = 0
    curr = arr[0]
    for i in range(0,len(arr) - 1, 1):
        if arr[i+1] > arr[i]:
            # depth increasing
            deeper += 1
        else:
            # level out
            depths += deeper
            deeper = 0
    
    depths += deeper
    return depths

def partTwo(arr):
    curr = 3
    t = 0
    while curr < len(arr):
        f = arr[curr - 1] + arr[curr - 2] + arr[curr - 3]
        s = arr[curr] + arr[curr - 1] + arr[curr - 2]
        if s > f:
            t += 1
        curr += 1

    return t    

if __name__ == "__main__":
    filename1 = 'advertDayOneP1Input.txt'
    filename2 = 'advertDayOneP1Input.txt'
    l = readInputFileNumbers(filename1)
    print(partOne(l))
    s = readInputFileNumbers(filename2)
    print(partTwo(s))
