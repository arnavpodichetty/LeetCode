class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        index = len(nums) - 1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            square_left = nums[left] * nums[left]
            square_right = nums[right] * nums[right]
            if square_left > square_right:
                squares[index] = square_left
                left += 1
            else:
                squares[index] = square_right
                right -= 1
            index -= 1
            
        return squares


"""
Brute Force
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])


Initial
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squares.insert(0, pow(nums[left], 2))
                left += 1
            elif abs(nums[left]) < abs(nums[right]):
                squares.insert(0, pow(nums[right], 2))
                right -= 1
            else:
                squares.insert(0, pow(nums[left], 2))
                left += 1
        return squares
"""