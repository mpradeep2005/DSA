from collections import deque
def bfs(node):
    q=deque()
    q.append(node)

    while q:
        node=q.popleft()
        print(node)
        for i in edge[node]:
            if i not in seen:
                seen.add(i)
                q.append(i)

edge=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
v=5
seen=set()
root=0
seen.add(0)
print(bfs(root))