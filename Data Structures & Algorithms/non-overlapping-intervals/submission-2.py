class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort(key=lambda interval : interval[1])
        min_start_time = intervals[0][1]
        count = 0
        for interval in intervals[1:]:
            if interval[0] >= min_start_time:
                min_start_time = interval[1]
            else:
                count += 1
        return count