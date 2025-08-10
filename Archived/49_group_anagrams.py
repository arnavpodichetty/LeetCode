class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        groups = []
        
        for s in strs:
            sorted_word = "".join(sorted(s))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(s)
            else:
                anagrams[sorted_word] = [s]
        
        for val in anagrams.values():
            groups.append(val)
        
        return groups