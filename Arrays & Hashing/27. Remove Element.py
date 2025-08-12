class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left


"""
Initial
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del(nums[i])
            else:
                k += 1
        
        return k
"""