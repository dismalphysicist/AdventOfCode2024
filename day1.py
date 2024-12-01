#!/usr/bin/env python3

def find_in_sorted_list(item,lst):
  # assume list is sorted
  # returns number of times the item was found
  # can easily be changed to return a list of locations
  occurs = 0
  for l in lst:
    if l < item:
      continue
    elif l > item:
      break
    if l == item:
      occurs += 1

  return occurs

list1 = []
list2 = []

with open("input1.txt","r") as f:
  input = f.read().strip().split("\n")
  # make our two lists by splitting by whitespace
  list1 = [int(l.split()[0]) for l in input]
  list2 = [int(l.split()[1]) for l in input]

list1.sort()
list2.sort()

# problem didn't specify whether distance was signed or not, I've assumed not
distances = [ abs(list2[i]-list1[i]) for i in range(len(list1)) ]
part1 = sum(distances)

print("Part 1: sum of distances =",part1)

# multiply by number of times item is in the other list
weighted = [ item*find_in_sorted_list(item,list2) for item in list1 ]

part2 = sum(weighted)

print("Part 2: sum of weighted numbers =",part2)