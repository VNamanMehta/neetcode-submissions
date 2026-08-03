class Solution:

    def encode(self, strs: List[str]) -> str:
        final_s = ''
        for s in strs:
            l = len(s)
            sub_s = str(l) + '#' + s
            final_s += sub_s
        return final_s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            word = s[j+1:j+1+l]
            res.append(word)
            i = j+1+l
        return res