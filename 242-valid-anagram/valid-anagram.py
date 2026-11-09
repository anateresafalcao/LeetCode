class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for char1, char2 in zip(s,t):
                if s.find(char2)==-1 or t.find(char1)==-1:
                    return False
                elif s.count(char2)>t.count(char2) or t.count(char1)>s.count(char1):
                    return False
            return True
        else:
            return False
       