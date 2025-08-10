class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majortiy_dict = {}
        
        for n in nums:
            if n in majortiy_dict:
                majortiy_dict[n] += 1
            else:
                majortiy_dict[n] = 1
        
        return max(majortiy_dict, key=majortiy_dict.get)