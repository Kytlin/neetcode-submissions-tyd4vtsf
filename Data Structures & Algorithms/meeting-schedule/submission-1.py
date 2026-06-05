"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        ordered_intervals = sorted(intervals, key=lambda interval : interval.start)

        cur_end_time = ordered_intervals[0].end
        for interval in ordered_intervals[1:]:
            if interval.start < cur_end_time:
                return False
            cur_end_time = interval.end
        return True