N, A, B = map(int, input().split())

ans = 0
if (N == 1 and A != B) or A > B:
    ans = 0
else:
    ans = (B-A)*(N-2)+1

print(ans)
