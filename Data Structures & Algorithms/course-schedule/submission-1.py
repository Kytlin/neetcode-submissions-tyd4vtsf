from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)

        visited = [0] * numCourses

        def dfs(course):
            if not adj_list[course]:
                return True

            visited[course] = 1
            for neighbour in adj_list[course]:
                if visited[neighbour] == 1 or not dfs(neighbour):
                    return False
            visited[course] = 0
            adj_list[course] = [] # this course returns true without traversal next time
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True