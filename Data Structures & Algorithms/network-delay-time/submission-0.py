class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for start, end, weight in times:
            adj_list[start].append((end, weight))

        visited = set()
        dist_arr = [float("inf")] * (n+1)
        dist_arr[k], min_dist = 0, -1
        pq = [(0, k)]
        while pq:
            dist, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                min_dist = dist

            for next_node, weight in adj_list[node]:
                if dist_arr[node] + weight < dist_arr[next_node]:
                    dist_arr[next_node] = dist_arr[node] + weight
                    heapq.heappush(pq, (dist_arr[next_node], next_node))

        return min_dist