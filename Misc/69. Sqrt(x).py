class Solution:
    def mySqrt(self, x: int) -> int:
        # Handles base case for x = 0 and x = 1
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        # Use <= for binary search
        while left <= right:
            middle = left + (right - left) // 2
            square = middle * middle
            if square == x:
                return middle
            # If square is less than target, then delete entire left side (all squares less than x)
            elif square < x:
                left = middle + 1
            # If square is greater than target, then delete entire right side (all squares greater than x)
            elif square > x:
                right = middle - 1
        return right


"""
Brute Force
class Solution:
    def mySqrt(self, x: int) -> int:        
        for i in range(x + 1):
            if i * i == x:
                return i
        
        for i in range(x + 1):
            if i * i > x:
                return i - 1
"""