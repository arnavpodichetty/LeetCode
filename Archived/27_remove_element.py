class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        right = len(nums) - 1
        k = 0

        for n in nums:
            if n != val:
                k += 1

        for i in range(len(nums)):
            if nums[i] == val:
                if i >= right:
                    break
                nums[i] = nums[right]
                nums[right] = val
                right -= 1
                if i == k - 1:
                    return k
        
        return k