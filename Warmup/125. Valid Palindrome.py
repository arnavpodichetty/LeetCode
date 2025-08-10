class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True


"""
Initial:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        
        for char in s.lower():
            if char.isalnum():
                chars.append(char)
        
        left, right = 0, len(chars) - 1
        
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
"""