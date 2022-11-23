from collections import defaultdict
from typing import Tuple


def create_net(array: Tuple[Tuple[str]])-> defaultdict:
    graph = defaultdict(set)
    
    # Fill in graph
    for i in array:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])
    return graph


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