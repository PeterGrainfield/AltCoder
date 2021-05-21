W, a, b = map(int, input().split())
ans = abs(b-a)
if ans <= W:
    print(0)
else:
    print(ans-W)