class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window = {}
        t_count = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        current_cond, needed = 0, len(t_count)

        res_ind, reslen = [0, 0], float("inf")

        l = 0

        for r in range(len(s)):
            # if s[r] in t_count:
            window[s[r]] = 1 + window.get(s[r], 0)

            if (s[r] in t_count) and (window[s[r]] == t_count[s[r]]):
                current_cond += 1

            while current_cond == needed:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res_ind = [l, r]

                window[s[l]] -= 1
                if (s[l] in t_count) and (window[s[l]] < t_count[s[l]]):
                    current_cond -= 1

                l += 1

        if reslen != float("inf"):
            l, r = res_ind
            return s[l:r+1]
        else:
            return ""
        