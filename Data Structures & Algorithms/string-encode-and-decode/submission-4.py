class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs:
            l = len(i)
            final_str += f"{l}#{i}"

        return final_str

    def decode(self, s: str) -> List[str]:
        final_list = []
        idx = 0
        
        while idx<len(s):
            l = ''
            while s[idx] != '#':
                l += s[idx]
                idx+=1
            print(l)
            word = s[idx+1: idx+1+int(l)]
            final_list.append(word)
            idx = idx+1+int(l)
        
        
        return final_list
