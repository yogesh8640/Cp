row=int(input())
mat=[]
for i in range(row):
    mat.append(list(map(int,input.split())))
col=len(mat[0])
res=[]

for i in range(row):
    for j in range(col-2):
        if mat[i][j]==mat[j][j+1]==mat[i][j+2]:
            res.append(mat[i][j])


for i in range(row-2):
    for j in range(col):
        if mat[i][j]==mat[i+1][j]==mat[i+2][j]:
            res.append[mat[i][j]

                       
for i in range(row-2):
    for j in range(col-2):
        if mat[i][j]==mat[i+1][j+1]==mat[i+2][j+2]:
            res.append(mat[i][j]

print(min(res))
