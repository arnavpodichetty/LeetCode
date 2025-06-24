class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set()
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in nums_set:
                return [nums.index(diff), i]
            
            nums_set.add(nums[i])
    