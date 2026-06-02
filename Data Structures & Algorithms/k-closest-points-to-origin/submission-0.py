class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_pts = []
        num_points = 0
        for x, y in points:
            heapq.heappush_max(closest_pts, [x**2+y**2, (x, y)])
            num_points += 1
            if num_points > k:
                heapq.heappop_max(closest_pts)
        return [pt for dist, pt in closest_pts]