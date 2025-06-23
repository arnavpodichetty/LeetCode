class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            n = nums[i]
            for j in range(i + 1, len(nums)):
                if n == nums[j]:
                    return True
                
        return False