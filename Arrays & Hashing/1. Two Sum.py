class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {nums[i]: i for i in range(len(nums))}
        
        for i in range(len(nums)):
            if target - nums[i] in prev and prev[target - nums[i]] != i:
                return [i, prev[target - nums[i]]]


"""
Brute Force
class Solution:
    def twoSum(self, nums: Lit[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""