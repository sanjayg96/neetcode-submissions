class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        maxf = 0
        l = 0
        len_dict = {}

        for r in range(len(s)):
            len_dict[s[r]] = len_dict.get(s[r], 0) + 1
            maxf = max(maxf, len_dict[s[r]])
            window_len = r - l + 1
            if (window_len - maxf) <= k:
                result = max(result, window_len)
            else:
                len_dict[s[l]] -= 1
                l += 1
                # if (r - l + 1 - maxf) <= k:
                #     result = max(result, window_len)


        return result