class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for succ, pred in prerequisites:
            adj_list[pred].append(succ)

        colours = [0] * numCourses
        possible = True
        def dfs(node):
            colours[node] = 1
            for neighbour in adj_list[node]:
                if colours[neighbour] == 0:
                    dfs(neighbour)
                elif colours[neighbour] == 1:
                    nonlocal possible
                    possible = False
                    return
            colours[node] = 2

        for course in range(numCourses):
            if colours[course] == 0:
                dfs(course)

        return possible