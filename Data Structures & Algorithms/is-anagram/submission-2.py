class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        if (sorted(s) == sorted(t)):
            return True
        else:
            return False