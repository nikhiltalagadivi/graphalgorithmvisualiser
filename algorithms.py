from collections import deque

def bfs(graph, start):
    q = deque([start])

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

def dfs(graph, start):
    q = deque([start])

    visited = set()

    while q:
        v = q.pop()

        if v in visited:
            continue
        visited.add(v)

        yield v, visited.copy()

        for e in graph.adj[v]:
            if e not in visited:
                q.append(e)