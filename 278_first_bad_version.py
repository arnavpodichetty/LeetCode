# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary_search(low, high):
            if high >= low:
                mid = (low + high) // 2
                
                if isBadVersion(mid):
                    if not isBadVersion(mid - 1) or mid == 1:
                        return mid
                    
                    return binary_search(low, mid - 1)
                else:
                    return binary_search(mid + 1, high)
            
        return binary_search(1, n)