class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0
        
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res


"""
Initial
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
                
        for n in counts:
            if counts[n] > len(nums) // 2:
                return n

Hash Map
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0
        
        for n in nums:
            count[n] += 1
            if count[n] > maxCount:
                res = n
                maxCount = count[n]
        return res
"""