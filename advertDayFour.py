lines = []
filename = "inputs/advertDayFourInput.txt" 
with open(file=filename, mode="r") as f:
  for line in f:
    lines.append(line.strip())

bingoNumbers = [int(x) for x in lines[0].split(",")]
grid = 5
boardSets = []

for i in range(2, len(lines), 6):
  tempBoard = []
  for n in range(grid):
    tempBoard.append([int(x) for x in lines[i + n].split(" ") if x != ""])
  boardSets.append(tempBoard)

boardPlays = []
for board in boardSets:
  boardPlays.append([[False for i in range(grid)] for j in range(grid)])

boardDone = [False for i in range(len(boardSets))]
  
for num in bingoNumbers:
  for bn, board in enumerate(boardSets):
    for y in range(grid):
      for x in range(grid):
        if board[y][x] == num:
          boardPlays[bn][y][x] = True
  
  for bn, boardplay in enumerate(boardPlays):
    if boardDone[bn]:
      continue
    win = False
    for column in range(grid):
      if all([boardplay[column][x] for x in range(grid)]):
        win = True
    for row in range(grid):
      if all([boardplay[y][row] for y in range(grid)]):
        win = True
    if win:
      s = 0
      for y in range(grid):
        for x in range(grid):
          if boardplay[y][x] == False:
            s += boardSets[bn][y][x]
      print(s * num)
      boardDone[bn] = True


