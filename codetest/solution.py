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

# print(isFlipedString("sdffs", "asdfd"))

class Solution(object):
    def tictactoe(self, board):
        """
        "O X",
        " XO",
        "X O"
        """

        n = len(board)
        def check(c):
            s = c * n
            return any((
                any(row == s for row in board),
                any(col == s for col in map("".join, zip(*board))),
                all(board[i][i] == c for i in range(n)),
                all(board[i][n-i-1] == c for i in range(n))
            ))
        
        if check("X"):
            return "X"
        if check("O"):
            return "O"
        if ' ' in ''.join(board):
            return "Pending"
        return "Draw"
    
    #  T9 LCCI
    def getValidT9Words(self, num, words):
        ans = []
        m = {"a":"2", "b":"2", "c":"2", "d":"3", "e":"3", "f":"3", "g":"4", "h":"4", "i":"4", "j":"5", "k":"5", "l":"5",
             "m":"6", "n":"6", "o":"6", "p":"7", "q":"7", "r":"7", "s":"7", "t":"8", "u":"8", "v":"8", "w":"9", "x":"9", "y":"9", "z":"9"}
        for word in words:
            print(word)
            numc = ""
            for c in word:
                num += m[c]
            if numc == num:
                ans.append(word)
        return ans
        
sol = Solution()
print(sol.tictactoe(["O X"," XO","X O"]))
        