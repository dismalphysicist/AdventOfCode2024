#!/usr/bin/env python3

import re

instructions = []
mul = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
num = r'[0-9]{1,3}'

with open("input3.txt","r") as f:
  instructions = re.findall(mul,f.read())

total = 0

# test = r'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

for i in range(len(instructions)):
  instructions[i] = [ int(n) for n in re.findall(num,instructions[i]) ]
  total += instructions[i][0]*instructions[i][1]

print(total)