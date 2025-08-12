# Hash Set
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = {}
        
        for char in sentence:
            if char not in seen:
                seen[char] = 1
            seen[char] += 1
        
        if len(seen) == 26:
            return True
        return False


"""
Initial
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = list("abcdefghijklmnopqrstuvwxyz")
        bool_array = [False] * 26
        
        for c in sentence:
            bool_array[letters.index(c)] = True
            
        if sum(bool_array) == 26:
            return True
        return False
"""