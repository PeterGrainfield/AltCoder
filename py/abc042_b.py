N, L = map(int, input().split())

ls = []
for i in range(N):
    ls.append(input())

ans = ""
ls.sort()
for s in ls:
    ans += s
print(ans)