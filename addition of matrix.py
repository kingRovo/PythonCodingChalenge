x=[[2,3,4],
   [4,5,3],
   [1,2,2]]
y=[[1,3,4],
   [4,4,3],
   [1,2,2]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]


for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j]+y[i][j]

for i in range(len(x)):
    for j in range(len(x[0])):
        print(r[i][j],end=' ')
    print(" ")
