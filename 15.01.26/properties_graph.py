def intersection(properties, i, j):
    setj = set(properties[j])
    return len([x for x in properties[i] if x in setj])

def dfs(graph, src, visited):
    visited[src] = True
    for neighbor in graph[src]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def number_of_components(properties, k):
    v = len(properties)
    graph = [[] for _ in range(v)]
    
    for i in range(v):
        for j in range(i + 1, v):
            if intersection(properties, i, j) >= k:
                graph[i].append(j)
                graph[j].append(i)
    
    count = 0
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
    return count
