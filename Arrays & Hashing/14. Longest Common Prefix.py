class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortestLength = min(len(string) for string in strs)
        
        for i in range(shortestLength):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix