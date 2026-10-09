class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for n, count in seen.items():
            buckets[count].append(n)
        
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
            