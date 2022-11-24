from collections import defaultdict
from typing import Tuple


def create_net(array: Tuple[Tuple[str]])-> defaultdict:
    graph = defaultdict(set)
    
    # Fill in graph
    for i in array:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])
    return graph