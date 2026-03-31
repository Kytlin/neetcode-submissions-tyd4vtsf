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
        visited = set()
        queue = deque()
        queue.append(src)

        while queue:
            cur = queue.popleft()
            if cur == dst:
                return True

            visited.add(cur)
            for neighbour in self.adj_list[cur]:
                if neighbour not in visited:
                    queue.append(neighbour)
        
        return False