N, K = map(int, input().split())
la = list(map(int, input().split()))

for i in range(K,N):
    if la[i-K] < la[i]:
        print("Yes")
    else:
        print("No")
