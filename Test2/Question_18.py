graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

v1 = "A"
v2 = "C"

if v2 in graph[v1]:
    print("Direct Edge Exists")
else:
    print("Direct Edge Does Not Exist")