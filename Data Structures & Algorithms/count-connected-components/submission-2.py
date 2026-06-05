class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list, count = defaultdict(set), 0
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        visited = [0] * n

        def dfs(cur_vrtx):
            for next_vrtx in adj_list[cur_vrtx]:
                if not visited[next_vrtx]:
                    visited[next_vrtx] = 1
                    dfs(next_vrtx)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(i)
                count += 1
        return count