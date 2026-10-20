from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [item for item, value in Counter(nums).most_common(k)]
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        heap = [(-count, num) for num, count in d.items()]
        heapq.heapify(heap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output