class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for i in strs:
            t = tuple(sorted(i))
            if t not in hm:
                hm[t] = []

            hm[t].append(i)
        return list(hm.values())