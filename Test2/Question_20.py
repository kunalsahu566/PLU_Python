graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

stack = ["A"]
visited = []

while stack:
    node = stack.pop()
    if node not in visited:
        print(node)
        visited.append(node)
        for i in reversed(graph[node]):
            if i not in visited:
                stack.append(i)