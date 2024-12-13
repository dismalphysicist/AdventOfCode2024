#!/usr/bin/env python3

import numpy as np
import re

# read in systems of linear equations as numpy ndarrays
with open("input13.txt","r") as f:
  machinesp1 = f.read().strip().split("\n\n")
  machinesp2 = machinesp1.copy()

machinesp1 = [ m.split("Prize") for m in machinesp1 ]
machinesp2 = [ m.split("Prize") for m in machinesp2 ]
  
for m in machinesp1:
  lines = m[0].split("\n")
  m[0] = np.array([re.findall(r'[0-9]+',lines[i]) for i in range(2)],dtype=int)
  m[0] = np.transpose(m[0])
  m[1] = np.array(re.findall(r'[0-9]+',m[1]),dtype=int)

for m in machinesp2:
  lines = m[0].split("\n")
  m[0] = np.array([re.findall(r'[0-9]+',lines[i]) for i in range(2)],dtype=int)
  m[0] = np.transpose(m[0])
  m[1] = np.array(re.findall(r'[0-9]+',m[1]),dtype=int)
  m[1] = m[1]+10000000000000


def solve(machines):
  total = 0
  check = 0
  # solve for number of presses and evaluate token cost
  for i,machine in enumerate(machines):
    try:
      presses = np.linalg.solve(machine[0],machine[1])
    except np.linalg.LinAlgError:
      print("No solution found, matrix is singular")
      continue

    tol = 1e-3
    if abs(presses[0]-round(presses[0]))<tol and abs(presses[1]-round(presses[1]))<tol:
      valid = True
      total += 3*round(presses[0])+round(presses[1])

  return total

totalp1 = solve(machinesp1)
totalp2 = solve(machinesp2)

print("Part 1: total tokens needed =",totalp1)
print("Part 2: with offset,",totalp2)