class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_track = set()
        result = 0
        l = 0

        for r in range(len(s)):
            while s[r] in set_track:
                set_track.remove(s[l])
                l += 1
            set_track.add(s[r])
            result = max(result, r - l + 1)

        return result
            