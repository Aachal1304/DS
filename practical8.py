from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Create Adjacency Matrix
nodes = list(graph.keys())
matrix = [[0] * len(nodes) for _ in nodes]

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if nodes[j] in graph[nodes[i]]:
            matrix[i][j] = 1

print("Adjacency Matrix:")
for row in matrix:
    print(row)


# DFS Traversal
def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            i = nodes.index(node)

            for j in range(len(nodes) - 1, -1, -1):
                if matrix[i][j] == 1 and nodes[j] not in visited:
                    stack.append(nodes[j])


# BFS Traversal
def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Main Program
print("\nDFS Traversal:")
dfs('A')

print("\nBFS Traversal:")
bfs('A')

print()