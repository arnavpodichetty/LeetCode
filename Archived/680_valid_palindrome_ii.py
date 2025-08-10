class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        count = 0
        
        while start < end:
            if s[start] != s[end]:
                count += 1
                if count > 1:
                    return False
                elif s[start + 1] == s[end]:
                    start += 1
                elif s[start] == s[end - 1]:
                    end -=1
                
            start += 1
            end -= 1
        
        return True