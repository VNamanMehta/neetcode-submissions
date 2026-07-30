class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lookup={}

        for i in s:
            lookup[i] = lookup.get(i,0)+1

        for i in t:
            if i not in lookup:
                return False

            lookup[i]-=1

        return all(i==0 for i in lookup.values())    