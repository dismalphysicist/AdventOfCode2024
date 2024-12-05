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
for update in updates:
  if passes_all(update,rules):
    totalp1 += update[int((len(update)-1)/2)]
  
print(totalp1)