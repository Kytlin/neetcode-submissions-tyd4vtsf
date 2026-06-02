class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        cur_weights = [-weight for weight in stones]
        heapq.heapify(cur_weights)

        while len(cur_weights) > 1:
            stone1_weight = heapq.heappop(cur_weights)
            stone2_weight = heapq.heappop(cur_weights)
            if stone1_weight != stone2_weight:
                heapq.heappush(cur_weights, -abs(stone1_weight - stone2_weight))

        return -cur_weights[0] if len(cur_weights) == 1 else 0