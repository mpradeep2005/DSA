from collections import deque
def bfs(node):
    q=deque()
    q.append(node)

    while q:
        node=q.popleft()
        print(node)
        for i in edge[node]:
            if i not in seen:
                q.append(i)
                seen.add(i)


edge=[
    [1],       # 0 connected to 1
    [0, 2],    # 1 connected to 0 and 2
    [1],       # 2 connected to 1
    [4],       # 3 connected to 4
    [3]        # 4 connected to 3
]
v=len(edge)

seen=set()
source=0
seen.add(source)
for i in range(v):
    if i not in seen:
        bfs(i)
    