class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or self.time_map[key][0][1] > timestamp:
            return ""
        if self.time_map[key][-1][1] <= timestamp:
            return self.time_map[key][-1][0]

        left, right = 0, len(self.time_map[key])-2
        while left <= right:
            mid = left + (right-left) // 2
            if self.time_map[key][mid][1] <= timestamp < self.time_map[key][mid+1][1]:
                return self.time_map[key][mid][0]
            if timestamp > self.time_map[key][mid][1]:
                left = mid + 1
            else:
                right = mid - 1