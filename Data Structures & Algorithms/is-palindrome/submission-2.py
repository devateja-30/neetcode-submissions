class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        n = len(s)
        # print("n",n)
        if n<2:
            return True
        if n==2:
            if s[0] != s[1]:
                return False
        for i in range (0,(n)//2):
            if s[i] != s[n-1-i]:
                return False
        return True