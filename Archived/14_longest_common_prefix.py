class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        pref_set = set()
        shortest = len(strs[0])
        
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
        
        for i in range(shortest):
            letter = strs[0][i]
            pref_set = set()
            for s in strs:
                pref_set.add(s[i])
                if len(pref_set) != 1:
                    return pref
            pref += letter
        
        return pref