N, D = map(int, input().split())

listX = []
for i in range(N):
    listX.append(list(map(int, input().split())))

cnt = 0
for i in range(N):

    for j in range(i+1, N):
        py = listX[i]
        pz = listX[j]
        dis = 0
        for k in range(D):
            dis += (py[k]-pz[k])**2
        if (dis ** 0.5).is_integer():
            cnt += 1
print(cnt)
