class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1 

        sorted_keys = sorted(count , key = count.get , reverse=True)
        return sorted_keys[:k]