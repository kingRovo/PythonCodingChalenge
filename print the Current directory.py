import os

addr="E:/python program/"
dirs=os.listdir(addr)
cnt=0
for file in dirs:
    print(file)
    cnt=cnt+1
print("There Are ",cnt,"files ")
    
