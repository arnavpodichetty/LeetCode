# Hash Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        
        for x in nums:
            if x in unique_set:
                return True
            unique_set.add(x)
            
        return False


"""
Brute Force
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


Sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sorted(nums) returns a copy
        # .sort() sorts in-place
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False     
"""