from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        for freq in count.values():
            if freq != 0:
                return False
        return True


"""
Initial
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        
        for c in s:
            if c in letters_s:
                letters_s[c] += 1
            else:
                letters_s[c] = 1
        
        for c in t:
            if c in letters_t:
                letters_t[c] += 1
            else:
                letters_t[c] = 1
        
        if dict(sorted(letters_s.items())) == dict(sorted(letters_t.items())):
            return True
        return False


Counter Collection
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""