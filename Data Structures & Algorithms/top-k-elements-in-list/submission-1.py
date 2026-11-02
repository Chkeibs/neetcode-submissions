class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ordered = sorted(
            counts,
            key=lambda x: counts[x],
            reverse=True
        )
        return(ordered[:k])  
