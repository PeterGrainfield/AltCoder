N = int(input())

A_list = []
for i in range(2):
    A_list.append(list(map(int, input().split())))

score = 0
down = 0
for i in range(N):
    sc = sum(A_list[0][0:i+1]) + sum(A_list[1][i:])
    score = max(score, sc)

print(score)
