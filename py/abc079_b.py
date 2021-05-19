N = int(input())

lryu = [2, 1]

for i in range(2, N+1):
    lryu.append(lryu[i-1] + lryu[i-2])

print(lryu[N])
