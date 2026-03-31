from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        self.adj_list = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())

    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        
        visited.add((src,dst))
        for neighbour in self.adj_list[src]:
            if (neighbour,dst) not in visited and self.hasPath(neighbour, dst):
                return True

        return False