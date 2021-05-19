N, X = map(int, input().split())
la = list(map(int, input().split()))

ans = []
for a in la:
    if a != X:
        ans.append(str(a))
print(" ".join(ans))
