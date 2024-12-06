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
with open("input6.txt","r") as f:
  map = f.read().strip().split("\n")
  numlines = len(map)

linelen = len(map[0])
for i in range(len(map)):
  map[i] = [ c for c in map[i] ]
# index as map[vertical][horizontal]

sposition= (-1,-1)
# find starting position and direction
# store coordinates as (horizontal,vertical)
for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j] == "^":
      sposition = (j,i)

position = sposition
sdirection = "up" # given
direction = sdirection
visited = set([sposition])

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
    # print("Leaving map")
    break

print("Part 1: visited",len(visited),"unique locations")

totalp2 = 0
for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j]!=".":
      continue
    # edit map
    map[i][j] = "#"
    # reset to start
    position = sposition
    direction = sdirection
    visitedp2 = set([(sposition,sdirection)])
    for ntries in range(10000): # prevent infinite loop
      newpos = forward(direction,position)
      if onmap(newpos):
        if map[newpos[1]][newpos[0]]=="#":
          # obstacle
          direction = turn(direction)
        else:
          # move forward
          position = newpos
          if (position,direction) in visitedp2:
            # infinite loop
            totalp2 += 1
            # print("Found infinite loop, current count is",totalp2)
            # undo change to map
            map[i][j] = "."
            break
          visitedp2.add((position,direction))
      else:
        # undo change to map
        map[i][j] = "."
        break

print("Part 2: number of looping positions is",totalp2)