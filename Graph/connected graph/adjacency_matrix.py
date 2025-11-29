def adj_mat(v,edge):
    mat=[[0 for i in range(v)]for j in range(v)]

    for i in range(v):
        for j in edge[i]:
            mat[i][j]=1
            mat[j][i]=1
    return mat 
edge=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
v=5
mat=adj_mat(v,edge)
for i in mat:
    print(*i)
