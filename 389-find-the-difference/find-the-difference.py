class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            count_t = t.count(char)
            count_s = s.count(char)
            if count_t > count_s:
                return char

