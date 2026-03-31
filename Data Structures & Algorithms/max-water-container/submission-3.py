class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        max_area = 0
        while start < end:
            max_area = max(max_area, min(heights[start], heights[end]) * (end - start))
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return max_area