class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)

        most_frequent = heapq.nlargest(
            k,
            num_counts.items(),
            key=lambda x: x[1]
        )
        result = [num for num, _ in most_frequent]
        
        return result