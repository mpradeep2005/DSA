def adj_mat(v,edge):
    lis=[[]for i in range(v)]

    for i in range(v):
        for j in edge[i]:
           
            lis[i].append(j)

    return lis

edge=[[0, 1], [0, 2], [1, 2]]
v=3
mat=adj_mat(v,edge)
for i in range(v):
    print(f"{i} :",end=" ")
    for j in mat[i]:
        print(j,end=" ")
    print()
