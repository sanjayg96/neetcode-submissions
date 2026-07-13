class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trackmap = {}

        for s in strs:

            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) not in trackmap:
                trackmap[tuple(count)] = []

            trackmap[tuple(count)].append(s)

        return list(trackmap.values())