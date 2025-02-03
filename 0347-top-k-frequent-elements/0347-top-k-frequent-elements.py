class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occur = defaultdict(int)
        for num in nums:
            num_occur[num] += 1
        
        sorted_dict = dict(sorted(num_occur.items(), key=lambda x:x[1], reverse=True))
        return list(sorted_dict.keys())[:k]
        