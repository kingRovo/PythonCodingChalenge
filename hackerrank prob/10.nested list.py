scores = {}
top2 = []

def logScore(score):
    global top2
    xs = [x for x in top2 if x < score] + [score] + [x for x in top2 if x > score]
    if (len(xs) > 2):
        scores.pop(xs[2], None)
        xs.pop()
    top2 = xs
    return score <= xs[-1]

for _ in range(int(input())):
    name = input()
    score = float(input())
    if (logScore(score)):
        scores[score] = scores.get(score,[]) + [name]

for name in sorted(scores[top2[1]]):
    print(name)


#input formate 
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39
