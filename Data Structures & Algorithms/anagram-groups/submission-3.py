class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = {}

        for s in strs:
            ch = [0]*26
            for i in s:
                idx = ord(i) - ord('a')
                ch[idx]+=1

            if tuple(ch) not in l:
                l[tuple(ch)] = []

            l[tuple(ch)].append(s)

        return list(l.values())
