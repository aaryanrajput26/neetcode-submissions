class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s)!=set(t):
            return False
        return sorted(s)==sorted(t)