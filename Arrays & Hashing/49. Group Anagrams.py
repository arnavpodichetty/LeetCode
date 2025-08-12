class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_counts = []
        groups = []
        
        for s in strs:
            counts = {}
            for char in s:
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
            str_counts.append(counts)
        
        temp = []
        i = 0
        
        while i < len(str_counts) - 1:
            if str_counts[i].items() == str_counts[i + 1].items():
                temp.append(strs[i])
                temp.append(strs[i + 1])
                i += 1
            else:
                groups.append(temp)
                temp.clear()
            i += 1

        return groups