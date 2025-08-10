# Initial
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("aeiouAEIOU")
        chars = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            while chars[left] not in vowels and left < right:
                left += 1
            while chars[right] not in vowels and left < right:
                right -= 1
            
            temp = chars[left]
            chars[left] = chars[right]
            chars[right] = temp
            left += 1
            right -= 1
            
        return "".join(chars)