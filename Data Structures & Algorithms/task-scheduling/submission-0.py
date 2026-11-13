from collections import Counter
import math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        counts = counter.most_common()
        total = 0
        max_count = counts[0][1]
        m = max_count
        for item, count in counts:
            if count == max_count:
                total += 1
        print(counts, total)
        return max((m - 1) * (n + 1) + total, len(tasks))