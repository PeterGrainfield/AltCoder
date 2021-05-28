N, M = map(int, input().split())
laa = [list(input()) for _ in range(N)]
lbb = [list(input()) for _ in range(M)]

ans = "No"
for i in range(N-M+1):
    for j in range(N-M+1):
        ok = True
        for k, v in enumerate(lbb):
            if v != laa[i+k][j:j+M]:
                ok = False
        if ok:
            ans = "Yes"
            break
print(ans)