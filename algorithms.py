from collections import deque

def bfs(graph, start):
    # create an empty queue
    q = deque([start])

    # create an empty set visited
    visited = set()

    while q:
        v = q.popleft()

        if v in visited:
            continue
        visited.add(v)

        yield v, visited.copy()

        for e in graph.adj[v]:
            if e not in visited:
                q.append(e)
