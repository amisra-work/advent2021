filename = "inputs/dayOne.txt" 
left, right = 0, 0 
pos = 0
negOnes = []
with open(file=filename, mode="r") as f:
    for line in f:
        for e in line:
            if e == '(':
                left += 1
            else:
                right += 1
            pos += 1
            if left - right == -1:
                negOnes.append(pos)


print(left - right)          
print(negOnes[0])
