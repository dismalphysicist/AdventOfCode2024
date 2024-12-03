#!/usr/bin/env python3

import re

# this regex matches the basic "mul\([0-9]{1,3},[0-9]{1,3}\)"
# but in addition puts the numbers in capture groups with ()
# and also (using the logical or |) matches the do and don't statements
# and puts the whole thing in a capture group
allinst = r"(mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\))"

inputstring = ""
with open("input3.txt","r") as f:
  inputstring = f.read()

# findall returns a list of tuples of capture groups
allinstructions = re.findall(allinst,inputstring)

totalp1 = 0
totalp2 = 0
multp2 = True
for ins in allinstructions:
  if "mul" in ins[0]:
    totalp1 += int(ins[1])*int(ins[2])
    if multp2:
      totalp2 += int(ins[1])*int(ins[2])
  elif ins[0]=="do()":
    multp2 = True
  elif ins[0]=="don't()":
    multp2 = False
  else:
    print("Parsing error")

print("Part 1: all multiply instructions gives",totalp1)
print("Part 2: using do and don'ts, we get",totalp2)