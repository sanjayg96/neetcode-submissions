class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        current_cond_count, required_cond_count = 0, len(t_dict)

        res, len_res = "", float("inf")

        window_dict = {}
        l = 0
        for r in range(len(s)):
            window_dict[s[r]] = window_dict.get(s[r], 0) + 1

            if (s[r] in t_dict) and (window_dict[s[r]] == t_dict[s[r]]):
                current_cond_count += 1

            while current_cond_count == required_cond_count:
                if (r - l + 1) < len_res:
                    res = s[l:r+1]
                    len_res = r - l + 1
                
                window_dict[s[l]] -= 1
                if (s[l] in t_dict) and (window_dict[s[l]] < t_dict[s[l]]):
                    current_cond_count -= 1
                
                l += 1

        return res if len_res != float("inf") else ""

                