class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for c in s:
            if c.isalnum(): #isalnum() checks if char is a-z or 0-9
                new_s += c.upper()
        
        start, end = 0, len(new_s) - 1 
        
        while start < end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
            
        return True