class Solution:
    def shortestDistance(self, words, word1, word2):
        shortest = len(words)
        pos1 = pos2 = -1
        
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            
            if abs(pos2 - pos1) < shortest and pos1 != -1 and pos2 != -1:
                shortest = abs(pos2 - pos1)
        
        return shortest


"""
Brute Force
class Solution:
    def shortestDistance(self, words, word1, word2):
        shortest = len(words)
        words1_indicies = []
        words2_indicies = []
        
        for i in range(0, len(words)):
            if words[i] == word1:
                words1_indicies.append(i)
            if words[i] == word2:
                words2_indicies.append(i)
            
        for i in range(len(words1_indicies)):
            for j in range(len(words2_indicies)):
                if abs(words1_indicies[i] - words2_indicies[j]) < shortest:
                    shortest = abs(words1_indicies[i] - words2_indicies[j])
        
        return shortest
"""