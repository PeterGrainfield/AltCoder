N = int(input())

if N % 2:
    print("No")

N2 = N/2
ashi = (4, 5, 13)

N3, spN2 = divmod(N2, (ashi[0]*ashi[1]*ashi[2]))

ebiMax = int(spN2//ashi[2])
caniMax = int(spN2//ashi[0]+1)
# print(ebiMax, caniMax)

for i in range(ebiMax, caniMax):
    for j in range(caniMax-i):
        for k in range(caniMax-(i+j)):
            print(i, j, k)
            if k*ashi[0] + j*ashi[1] + i * ashi[2] == spN2:
                # print(i, j, k)
                print(k+j)
                exit()
else:
    print(0)
