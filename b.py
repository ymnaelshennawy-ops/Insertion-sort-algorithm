from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        if start not in self.graph:
            return []
        visited = set()
        queue = deque([start])
        result = []
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs_iterative(self, start):
        if start not in self.graph:
            return []
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

def test_graph():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    
    print("BFS from 1:", g.bfs(1))
    print("DFS from 1:", g.dfs_iterative(1))

if __name__ == "__main__":
    test_graph()