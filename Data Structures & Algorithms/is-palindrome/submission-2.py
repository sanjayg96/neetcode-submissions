class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = s.lower()
        l, r = 0, len(newstr) - 1
        while l < r:
            while not newstr[l].isalnum():
                l += 1
                if l == len(newstr):
                    return True
            while not newstr[r].isalnum():
                r -= 1
                if r < 0:
                    return True
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1

        return True
