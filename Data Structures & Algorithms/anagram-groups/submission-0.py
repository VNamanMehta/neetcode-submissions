class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in strs:
            c = [0]*26
            
            for ch in i:
                idx = ord(ch) - ord('a')
                c[idx]+=1
            
            k = tuple(c)
            if k not in hm:
                hm[k] = []
            hm[k].append(i)

        return list(hm.values())

