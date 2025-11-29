def dfs(node):
    print(node)
    for i in lis[node]:
        if i not in seen:
            seen.add(i)
            dfs(i)

def adj_lis(v,edge):
    lis=[[]for i in range(v)]

    for i in range(v):
        for j in edge[i]:
            lis[i].append(j)
    return lis

edge=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
v=5
lis=adj_lis(v,edge)
root=0
seen=set()
seen.add(root)
dfs(root)