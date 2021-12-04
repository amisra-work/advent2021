filename = "/Users/amisra/workspace/advent2021/problems2015/inputs/dayTwo.txt" 

presents = []
with open(filename) as f:
    for line in f:
        presents.append([int(y) for y in line.split('x')])

squareFeetVerbose = 0

for gift in presents:
    l,w,h = gift
    slack = min((l*w), (l*h))
    slack = min(slack, (w*h))
    actual = (2*l*w) + (2*w*h) + ( 2*h*l)
    squareFeetVerbose += (slack + actual)

squareFeetConservatiive = 0
for gift in presents:
    l,w,h = gift
    min1 = min(l,h,w)
    min2 = 0
    if min1 == l:
        min2 = min(h, w)
    if min1 == w:
        min2 = min(h, l)
    if min1 == h:
        min2 = min(l, w)
    

    actual = ((2* min1) + (2 * min2) ) + (l * w * h)
    squareFeetConservatiive +=  actual



print(squareFeetVerbose)
print(squareFeetConservatiive)

