class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        num_intervals = len(intervals)
        output = [intervals[0]]
        for i in range(1, num_intervals):
            interval_a = output.pop()
            interval_b = intervals[i]
            a0, a1 = interval_a
            b0, b1 = interval_b
            if a1 >= b0:
                output.append([a0, max(b1, a1)])
            else:
                output.append(interval_a)
                output.append(interval_b)
        return output


        