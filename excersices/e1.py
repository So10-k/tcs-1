import random
import time
import os
rl = [1,5,56,75,23,5,9,6]
index = -1
max = -1
# for i in rl:
#     if(i > max):
#         max = i
#         index+=1
# print(max)
# print(index)


for i in range(len(rl)):
    if(rl[i] > max):
        max = rl[i]
        index = i
print(max)
print(index)