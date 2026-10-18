class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        b = 0
        for i in nums:
            if i - 1 not in h:
                start = i
                t = 1
                while start+t in h:
                    t+=1
                b = max(b,t)
        return b