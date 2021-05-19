N, K = map(int, input().split())
la = list(map(int, input().split()))

idx = la.index(1)

left = idx
right = N - idx - 1
ans = 0
while left > 0 or right > 0:
    remain = K - 1
    if ans == 0:
        if left < remain:
            m = min(left, remain)
            remain -= m
            left -= m
            m = min(right, remain)
            remain -= m
            right -= m
        elif right < remain:
            m = min(right, remain)
            right -= m
            remain -= m
            m = min(left, remain)
            remain -= m
            left -= m

    if left > 0:
        m = min(left, remain)
        remain -= m
        left -= m
    elif right > 0:
        m = min(right, remain)
        remain -= m
        right -= m

    ans += 1
print(ans)
