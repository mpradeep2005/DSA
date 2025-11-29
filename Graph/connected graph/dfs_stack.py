def dfs(node):
    stack=[]
    stack.append(node)

    while stack:
        node=stack.pop()
        print(node)
        for i in edge[node]:
            if i not in seen:
                seen.add(i)
                stack.append(i)

edge=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
v=5
root=0
seen=set()
seen.add(root)
dfs(root)