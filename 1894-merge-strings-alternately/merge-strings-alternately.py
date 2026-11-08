class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = str()

        for char1, char2 in zip(word1, word2):
            merged = merged + char1 + char2
        
        if len(word1) > len(word2):
            merged = merged + word1[len(word2):]
            return merged
        elif len(word2) > len(word1):
            merged  = merged + word2[len(word1):]
            return merged
        else:
            return merged

