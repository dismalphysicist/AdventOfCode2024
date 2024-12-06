#!/usr/bin/env python3

directions = ["up","right","down","left"]

def forward(dir,pos):
  # pos must be a list or tuple of 2 elements
  # (horizontal index, vertical index)
  go = [(pos[0],pos[1]-1),(pos[0]+1,pos[1]),(pos[0],pos[1]+1),(pos[0]-1,pos[1])]
  i = directions.index(dir)
  return go[i]

def turn(dir):
  i = directions.index(dir)
  return directions[(i+1)%len(directions)]

def onmap(pos):
  if pos[0]>=0 and pos[0]<linelen and pos[1]>=0 and pos[1]<numlines:
    return True
  else:
    return False

# read input
with open("test6.txt","r") as f:
  map = f.read().strip().split("\n")
  numlines = len(map)

linelen = len(map[0])+1
for i in range(len(map)):
  map[i] = [ c for c in map[i] ]
# index as map[vertical][horizontal]

position= (-1,-1)
# find starting position and direction
# store coordinates as (horizontal,vertical)
for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j] == "^":
      position = (j,i)

direction = "up" # given
visited = set([position])

# implement movement
for ntries in range(10000): # prevent infinite loop
  newpos = forward(direction,position)
  if onmap(newpos):
    if map[newpos[1]][newpos[0]]=="#":
      # obstacle
      direction = turn(direction)
    else:
      # move forward
      position = newpos
      visited.add(position)
  else:
    print("Leaving map")
    break

print("Part 1: visited",len(visited),"unique locations")

# part 2 
# to add new obstacle, can just modify map 
# try running same code passing in different maps 
# to detect loop: if position is already in visited,
# AND direction is the same, we are in a loop
# -> need to store direction in visited