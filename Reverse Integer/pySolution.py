class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        
        is_negative = False
        
        if(x < 0):
            x = x * -1
            is_negative = True
        
        reverse = 0
        while(x != 0):
            digit = x % 10
            x //= 10
            
            if(reverse > INT_MAX / 10 or reverse == INT_MAX and digit > 7):
                return 0
            if(reverse < INT_MIN / 10 or reverse == INT_MIN and digit < -8):
                return 0
            reverse = reverse * 10 + digit
        
        if(is_negative):
            reverse *= -1
        
        return reverse
