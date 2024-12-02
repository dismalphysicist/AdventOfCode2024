#!/usr/bin/env python3

reports = []

with open("input2.txt","r") as f:
  reports = [ r.split() for r in f.read().strip().split("\n") ]
  for i in range(len(reports)):
    reports[i] = [ int(n) for n in reports[i]]

def monotonic(seq):
  # returns true if the sequence is monotonically increasing or decreasing
  if sorted(seq) == seq:
    return True
  elif sorted(seq,reverse=True) == seq:
    return True
  else:
    return False

def check_diffs(seq):
  for i in range(len(seq)-1):
    if abs(seq[i+1]-seq[i]) in range(1,4):
      continue
    else:
      return False
  return True

def get_subsets(lst):
  subs = []
  for i in range(len(lst)):
    copylst = lst.copy()
    del copylst[i]
    subs.append(copylst)
  return subs

totalp1 = 0
totalp2 = 0
# process reports 
for report in reports:
  if monotonic(report) and check_diffs(report):
    totalp1 += 1
    totalp2 += 1
    continue
  safe = False
  for rsub in get_subsets(report):
    if monotonic(rsub) and check_diffs(rsub):
      safe = True
  if safe:
    totalp2 += 1

print("Part 1: number of safe reports =",totalp1)
print("Part 2: with problem dampener =",totalp2)