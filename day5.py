#!/usr/bin/env python3

def passes(update,rule):
  try:
    index0 = update.index(rule[0])
    index1 = update.index(rule[1])
  except ValueError:
    index0 = -1
    index1 = -1
  if index0!=-1 and index1<index0:
    return False
  else:
    return True

def passes_all(update,rules):
  for rule in rules:
    if not passes(update,rule):
      # print("Fails rule",rule,": update",update)
      return False
  # print(update,": passes all rules")
  return True

def fix(update,rules):
  # implement topological sort using Kahn's algorithm
  # copy list of rules to modify, only keeping relevant ones
  starts = [ rule[0] for rule in rules if (rule[0] in update and rule[1] in update) ]
  ends = [ rule[1] for rule in rules if (rule[0] in update and rule[1] in update) ]
  # build list of page numbers which are not the second item of any rule
  S = [ n for n in update if n not in ends ]
  # loop
  L = []
  while len(S) > 0:
    # can vary pop index here to implement S as a queue or a stack
    # but this creates non-unique solutions 
    # so I suspect the puzzle input only admits 1 element to S initially
    n = S.pop()
    L.append(n)
    # for each m which is the second item of a rule starting n:
    nrules = [ i for i, x in enumerate(starts) if x == n ]
    for i in nrules:
      # remove the rule n|m
      starts[i] = -1
      m = ends[i]
      ends[i] = -1
      # if m is not the second item of any other rules, add m to S
      if m not in ends:
        S.append(m)
  # check for remaining rules
  for i in range(len(starts)):
    if starts[i] != -1 or ends[i] != -1:
      print("Error, there are still rules remaining")
  return L

# read input
with open("input5.txt","r") as f:
  rules, updates = f.read().strip().split("\n\n")

# process rules
rules = rules.split("\n")
for i in range(len(rules)):
  rules[i] = (int(rules[i].split("|")[0]), int(rules[i].split("|")[1]))
# process updates
updates = updates.split("\n")
for i in range(len(updates)):
  updates[i] = [ int(n) for n in updates[i].split(",") ]

# loop and add up
totalp1 = 0
totalp2 = 0
fails = []
for update in updates:
  if passes_all(update,rules):
    totalp1 += update[int((len(update)-1)/2)]
  else:
    fails.append(update)
  
print("Part 1: sum of middle numbers of all passing updates:",totalp1)

# loop for part 2
fails = [ fix(update,rules) for update in fails ]
for update in fails:
  totalp2 += update[int((len(update)-1)/2)]

print("Part 2: sum of middle numbers of all fixed updates:",totalp2)