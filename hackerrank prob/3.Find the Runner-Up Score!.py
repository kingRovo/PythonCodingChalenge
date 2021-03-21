n = int(input())
arr = list(map(int, input().split()))
up = max(arr)
for i in arr:
    if(i==up):
        arr.remove(max(arr))
print(max(arr))
