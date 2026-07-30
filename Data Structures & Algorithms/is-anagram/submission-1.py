class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)
        c1 = {}
        c2 = {}

        if len(s) != len(t):
             return False

        for i in s:
            c1[i] = c1.get(i, 0) + 1
        
        for i in t:
            c2[i] = c2.get(i, 0) + 1
        
        for i in c1:
            if i not in c2 or c2[i] != c1[i]:
                return False
        return True

        # if len(s) != len(t):
        #     return False

        # lookup={}

        # for i in s:
        #     lookup[i] = lookup.get(i,0)+1

        # for i in t:
        #     if i not in lookup:
        #         return False

        #     lookup[i]-=1

        # return all(i==0 for i in lookup.values())    