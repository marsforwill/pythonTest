from collections import Counter

# leetcode : Check Permutation LCCI
def CheckPermutation(s1, s2):
        print("this is test")
        return Counter(s1) == Counter(s2)
    
# print(CheckPermutation("abc", "cba"))

# String to URL LCCI
def replaceSpaces(S, length):
        return S[:length].replace(" ", "%20")

print(replaceSpaces("sdf ", 4))