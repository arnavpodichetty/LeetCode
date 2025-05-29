class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0
        count = 0
        
        while x > 0:
            count += 1
            x //= 10
        
        x = original

        for i in range(count):
            reversed += (x % 10) * (10 ** (count - i - 1))
            x //= 10

        return original == reversed