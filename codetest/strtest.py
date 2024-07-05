import re #regex


s = "hello"
word = ["hello", "world"]
print(type(s))
print(s[0])  # 输出: 'h'
print(s[1:4])  # 输出: 'ell'
print(len(s))
print(s + "work")
print("".join(word))
print(s.find("ll"))

name = "Alice"
age = 30
s = "Name: {}, Age: {}".format(name, age)
print(s)  # 输出: 'Name: Alice, Age: 30'

s = "The price is $100"
match = re.search(r'\$\d+', s)
if match:
    print(match.group())  # 输出: '$100'

str = "asdf"
for i in str:
    print("{}".format(i))



