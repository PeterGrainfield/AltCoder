K = int(input())
A, B = map(int, input().split())

for mul in range(K, B+1, K):
    if A <= mul and B >= mul:
        print("OK")
        break
else:
    print("NG")
