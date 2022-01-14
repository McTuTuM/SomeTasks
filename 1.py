# n = int(input())
n = 3 
temp = 0 
matr = []
max_num = matr[0][0]
for i in range(n):
    for j in range(n):
        if max_num < matr[i][j]:
            max_num = matr[i][j]
print(max_num)