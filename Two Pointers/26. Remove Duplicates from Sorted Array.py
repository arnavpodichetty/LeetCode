# Two Pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDuplicate = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[nextNonDuplicate - 1]:
                nums[nextNonDuplicate] = nums[i]
                nextNonDuplicate += 1
        
        return nextNonDuplicate


"""
Initial
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
"""