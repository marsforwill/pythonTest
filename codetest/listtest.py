from collections import Counter
from collections import deque
# * namedtuple   factory function for creating tuple subclasses with named fields
# * deque        list-like container with fast appends and pops on either end
# * ChainMap     dict-like class for creating a single view of multiple mappings
# * Counter      dict subclass for counting hashable objects
# * OrderedDict  dict subclass that remembers the order entries were added
# * defaultdict  dict subclass that calls a factory function to supply missing values
# * UserDict     wrapper around dictionary objects for easier dict subclassing
# * UserList     wrapper around list objects for easier list subclassing
# * UserString   wrapper around string objects for easier string subclassing
import heapq

# 创建 访问 修改 添加删除
lst = [1, 2, 3, "four", 5.0]
print(lst)  # 输出: [1, 2, 3, 'four', 5.0]
print(lst[3])  # 输出: 1
lst[3] = 4
lst.pop()
lst.append(6)
print(lst)  # 输出: [10, 2, 3, 4, 5]

sq = [ i**2 for i in range(10)]
print(sq)
sqlist = list(map(lambda x: x+2, sq))
print(sqlist)
even_lst = list(filter(lambda x: x % 2 == 0, sq))
print(even_lst)

heapq.heapify(sqlist)
print(sqlist)
count = Counter(lst)
print(count) 
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)

# tuple 元组 不可变的有序集合
tup = (1, 2, 3, "four", 5.0)
print(tup)  # 输出: (1, 2, 3, 'four', 5.0)
# 访问元素
print(tup[0])  # 输出: 1
