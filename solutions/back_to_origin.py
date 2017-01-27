#!/bin/python3

import sys


xTreasure,yTreasure = input().strip().split(' ')
xTreasure,yTreasure = [int(xTreasure),int(yTreasure)]
n = int(input().strip())
direction = []
for direction_i in range(n):
   direction_t = [int(direction_temp) for direction_temp in input().strip().split(' ')]
   direction.append(direction_t)
# your code goes here

# print("xt and yt", xTreasure, yTreasure )
# print(type(direction))
# print(direction)

xt, yt = xTreasure, yTreasure
# direction = [[0, 1], [1, 0]]


for i in range(len(direction)-1,-1,-1):
    # print(direction[i], direction[i][0], direction[i][1])
    xt -= direction[i][0]
    yt -= direction[i][1]

print(xt, yt)


