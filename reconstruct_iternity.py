from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    d = {}
    for i in tickets:
        if i[0] in d:
            d[i[0]].append(i[1])
            d[i[0]].sort()
        else:
            d[i[0]] = [i[1]]
    visited = []
    out = ['JFK']
    dfs(visited, d, 'JFK', out)
    return out
def dfs(visited, graph, node, out):
    try:
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                out.append(neighbour)
                dfs(visited, graph, neighbour, out)
    except KeyError:
        graph[node] = []


print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))