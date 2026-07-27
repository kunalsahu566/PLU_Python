graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

queue = ["A"]
visited = []

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            if i not in visited:
                queue.append(i)