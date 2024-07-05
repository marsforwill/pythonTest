
import math
import itertools # 迭代运算
import random
import numpy as np #数组 矩阵运算

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

a = math.sqrt(16)
print(type(a))
b = 1
print(type(b))
print(distance(1,1,4,5))
permutation = itertools.permutations([1,2,3])
for i in permutation:
    print(i)
print(random.randint(1,10))
arr = np.array([1,2,3,4,5])
print(arr)
print(np.sum(arr))