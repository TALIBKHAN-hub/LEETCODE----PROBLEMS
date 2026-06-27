class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(s,l,r):
            while(l>=0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        result = ""
        
        for i in range(len(s)):
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
        
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        
        return result
