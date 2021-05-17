def is_divisible(n):
    s=sum(list(map(int,str(n))))
    if n % s==0:
        return True
    else:
        return False
row,col=list(map(int,input().split()))
matrix=[]
for i in range(row):
    matrix.append(list(map(int,input().split())))
for r in range(row-1):#3
    for c in range(col-1):#2
        if(is_divisible(matrix[r][c]) and is_divisible(matrix[r][c+1]) and is_divisible(matrix[r+1][c]) and is_divisible(matrix[r+1][c+1])):
            print(matrix[r][c],matrix[r][c+1])
            print(matrix[r+1][c],matrix[r+1][c+1])
