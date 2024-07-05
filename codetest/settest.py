from collections import Counter

s = {1,2,3,4,5} # s = set([1, 2, 3, 4, 5])
print(s)
s.add(6)
s.remove(3)
print(s) 
print(3 in s)
print(Counter(s))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)  # 并集: {1, 2, 3, 4, 5}
print(s1 & s2)  # 交集: {3}
print(s1 - s2)  # 差集: {1, 2}
print(s1 ^ s2)  # 对称差集: {1, 2, 4, 5}

# 不可变
fs = frozenset([1, 2, 3])
print(fs)

def contains_duplicate(nums):
    return len(nums) != len(set(nums))
print(contains_duplicate([1,2,3,1]))

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
print(intersection({1,2,3},{1,2,4}))

