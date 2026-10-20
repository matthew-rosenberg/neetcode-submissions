class Solution:
    def maxArea(self, heights: List[int]) -> int:
        LENGTH = len(heights)
        i = 0
        j = LENGTH - 1
        max_volume = 0
        while j > i:
            H1 = heights[i]
            H2 = heights[j]
            volume = (j - i) * min(H1, H2)
            if volume > max_volume:
                max_volume = volume
            if H1 > H2:
                j -= 1
            else:
                i += 1
        return max_volume
