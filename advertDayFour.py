painfulInputForTheDay = []
filename = "inputs/advertDayFourInput.txt" 

with open(file=filename, mode="r") as f:
  for line in f:
    painfulInputForTheDay.append(line.strip())

bingoNumbers = [int(x) for x in painfulInputForTheDay[0].split(",")] # grab for line
grid = 5
boardSets = []

for i in range(2, len(painfulInputForTheDay), 6): # 1st line bingoNumbers, 2nd is blank line 3rd is start of board
  tempBoard = []
  for n in range(grid):
    tempBoard.append([int(x) for x in painfulInputForTheDay[i + n].split(" ") if x != ""]) # this wonderful logic to basically for creating a 5x5 grid
  boardSets.append(tempBoard)

boardPlays = [] # create board of plays cuz I did not wanna mod the original 
for board in boardSets:
  boardPlays.append([[False for k in range(grid)] for j in range(grid)]) 

doneMeBoard = [False for i in range(len(boardSets))] # insert the ones that be done 
outputs = []  
for num in bingoNumbers:
  for bn, board in enumerate(boardSets):
    for y in range(grid):
      for x in range(grid):
        if board[y][x] == num:
          boardPlays[bn][y][x] = True
  
  for bn, boardplay in enumerate(boardPlays): # built-in counting =) 
    if doneMeBoard[bn]: # continue looping cuz we just gonna solve all of them 
      continue
    win = False
    # checking for win =\
    for column in range(grid):
      if all([boardplay[column][x] for x in range(grid)]):
        win = True
    for row in range(grid):
      if all([boardplay[y][row] for y in range(grid)]):
        win = True
    if win:
      sumOfNotUsed = 0
      for y in range(grid):
        for x in range(grid):
          if boardplay[y][x] == False:
            sumOfNotUsed += boardSets[bn][y][x]
      outputs.append(sumOfNotUsed * num) # first and last output is the only ones we care about
      doneMeBoard[bn] = True

print(outputs[0],outputs[-1],sep='\n')
