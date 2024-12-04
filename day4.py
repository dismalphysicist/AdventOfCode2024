#!/usr/bin/env python3

def generate_mas_pos(xpos,numlines,linelen):
  mpos = []
  start, end, top, bottom = False, False, False, False
  if xpos%linelen<3:
    start = True
  elif xpos%linelen>linelen-4:
    end = True
  if xpos<linelen*3:
    top = True
  elif xpos>=linelen*(numlines-3):
    bottom = True
  
  # move m spaces right and n spaces down
  move = lambda m, n : i + m + n*linelen
  if not start:
    mpos.append([move(-1,0),move(-2,0),move(-3,0)])
  if not end:
    mpos.append([move(1,0),move(2,0),move(3,0)])
  if not top:
    mpos.append([move(0,-1),move(0,-2),move(0,-3)])
    if not start:
      mpos.append([move(-1,-1),move(-2,-2),move(-3,-3)])
    if not end:
      mpos.append([move(1,-1),move(2,-2),move(3,-3)])
  if not bottom:
    mpos.append([move(0,1),move(0,2),move(0,3)])
    if not start:
      mpos.append([move(-1,1),move(-2,2),move(-3,3)])
    if not end:
      mpos.append([move(1,1),move(2,2),move(3,3)])

  return mpos

def generate_ms_pos(apos,numlines,linelen):
  if apos%linelen > 0 and apos%linelen < linelen-1 and apos >= linelen and apos < linelen*(numlines-1):
    # return diagonal positions: top left, top right, bottom left, bottom right
    # need to check that M or S occur in each
    return [apos-linelen-1,apos-linelen+1,apos+linelen-1,apos+linelen+1]
  else:
    return []

wordsearch = ""
numlines = 0

with open("input4.txt","r") as f:
  wordsearch = f.read().strip()
  numlines = len(wordsearch.split("\n"))

linelen = len(wordsearch.split("\n")[0])+1

totalp1 = 0
# find all X's
Xs = [i for i, letter in enumerate(wordsearch) if letter == "X"]

# find all possible extensions of the word that don't go off the board
# & check whether M, A and S exist in that direction
for i in Xs:
  MASpos = generate_mas_pos(i,numlines,linelen)
  for arr in MASpos:
    if wordsearch[arr[0]]=="M" and wordsearch[arr[1]]=="A" and wordsearch[arr[2]]=="S":
      totalp1 += 1

totalp2 = 0
# find all A's
As = [i for i, letter in enumerate(wordsearch) if letter == "A"]
for i in As:
  # we get top left, top right, bottom left, bottom right
  MSpos = generate_ms_pos(i,numlines,linelen)
  if len(MSpos)==0:
    continue
  # check Ms on left side
  elif wordsearch[MSpos[0]]=="M" and wordsearch[MSpos[2]]=="M":
    if wordsearch[MSpos[1]]=="S" and wordsearch[MSpos[3]]=="S":
      totalp2 += 1
  # check Ms on top
  elif wordsearch[MSpos[0]]=="M" and wordsearch[MSpos[1]]=="M":
    if wordsearch[MSpos[2]]=="S" and wordsearch[MSpos[3]]=="S":
      totalp2 += 1
  # check Ms on right 
  elif wordsearch[MSpos[1]]=="M" and wordsearch[MSpos[3]]=="M":
    if wordsearch[MSpos[0]]=="S" and wordsearch[MSpos[2]]=="S":
      totalp2 += 1
  # check Ms on bottom
  elif wordsearch[MSpos[2]]=="M" and wordsearch[MSpos[3]]=="M":
    if wordsearch[MSpos[0]]=="S" and wordsearch[MSpos[1]]=="S":
      totalp2 += 1

print("Part 1: total number of occurrences of XMAS is",totalp1)
print("Part 2: total number of MAS crosses is",totalp2)