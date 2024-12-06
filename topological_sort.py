from collections import deque

def topologicalSortDfs(adjList):
    TS = []
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adjList[node]:
            dfs(neighbor)
        TS.append(node)

    for n in adjList.keys():
        if n not in visited:
            dfs(n)

    return list(reversed(TS))

def topologicalSortKahn(adjList):
    V = len(adjList.keys())
    indegree = {}
    for u, vs in adjList.items():
        if u not in indegree:
            indegree[u] = 0
        for v in vs:
            if v in indegree:
                indegree[v] += 1
            else:
                indegree[v] = 1
    q = deque()
    for v, count in indegree.items():
        if count == 0:
            q.append(v)
    TS = []
    while q:
        u = q.popleft()
        TS.append(u)
        for v in adjList[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return TS

def verify(adjList, topoSort):
    position = {n: i for i, n in enumerate(topoSort)}
    for v, neighbors in adjList.items():
        for n in neighbors:
            if position[v] >= position[n]:
                return False
    return True

if __name__ == "__main__":
    adjList = {
        0: [],
        1: [],
        2: [3],
        3: [4],
        4: [0, 1, 6],
        5: [0, 2],
        6: []
    }
    print("---DFS---")
    dfsSol = topologicalSortDfs(adjList)
    print(dfsSol, verify(adjList, dfsSol))
    print("---Kahns Algo---")
    khanSol = topologicalSortKahn(adjList)
    print(khanSol, verify(adjList, khanSol))
