#program to multiply two matrices using nested loops

a=[[3,6,9],
   [2,7,3],
   [8,4,2]]

b=[[6,8,1,2],
   [3,7,3,0],
   [8,5,9,1]]

#result is 3x4
res=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

for l in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            res[l][j]+=a[l][k]*b[k][j]


for r in res:
    print(r)
