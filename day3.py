#!/usr/bin/env python3

import re

allinstructions = []
mul = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
num = r'[0-9]{1,3}'

with open("input3.txt","r") as f:
  allinstructions = re.findall(mul,f.read())

totalp1 = 0

# test = r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

for i in range(len(allinstructions)):
  allinstructions[i] = [ int(n) for n in re.findall(num,allinstructions[i]) ]
  totalp1 += allinstructions[i][0]*allinstructions[i][1]

print("Part 1: all multiply instructions gives",totalp1)