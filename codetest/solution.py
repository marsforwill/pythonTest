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

# print(canPermutePalindrome("tactcoa"))

# Compress String LCCI
def compressString(S: str) -> str:
    if not S:
        return ""
    ch = S[0]
    ans = ''
    cnt = 0
    for c in S:
        if c == ch:
            cnt += 1
        else:
            ans += ch + str(cnt)
            ch = c
            cnt = 1
    ans += ch + str(cnt)
    return ans if len(ans) < len(S) else S

# print(compressString("aaaabbbc"))

# String Rotation LCCI
def isFlipedString(s1, s2):
    # return s2 in s1 + s1
    s = {s1}
    l = len(s1)
    if len(s2) != l:
        return False
    temp = s1
    for i in range(l):
        temp2 = temp[1:] + temp[0]
        s.add(temp2)
        temp = temp2
    print(s)
    return True if s2 in s else False


print(isFlipedString("sdffs", "asdfd"))

        