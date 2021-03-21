N = int(input())
score = 0
for i in range(N):
    line = input()
    match=line.find('=', 0)
    while(match >-1):
        match = line.find('=', match+1)
        score = score+1
print(score)
