from collections import Counter

# leetcode : Check Permutation LCCI
def CheckPermutation(s1, s2):
    print("this is test")
    return Counter(s1) == Counter(s2)
    
# print(CheckPermutation("abc", "cba"))

# String to URL LCCI
def replaceSpaces(S, length):
    return S[:length].replace(" ", "%20")

# print(replaceSpaces("sdf ", 4))

# Palindrome Permutation LCCI
def canPermutePalindrome(S):
    c = Counter(S)
    print(c)
    sum = 0
    for key in c:
        print(c[key])
        if c[key] % 2 == 1:
            sum+=1
    if sum <= 1:
        return True
    else: 
        return False

print(canPermutePalindrome("tactcoa"))
