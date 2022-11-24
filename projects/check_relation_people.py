from collections import defaultdict

def check_relation(graph: defaultdict, first: str, second: str)-> bool:
    visited = set()

    # ВFS
    queue = [first]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

    return True if second in visited else False