class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for c in s:
            if c.isalnum(): #isalnum() checks if char is a-z or 0-9
                new_s += c.upper()
        
        return new_s == new_s[::-1]