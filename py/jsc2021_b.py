N, M = map(int, input().split())
sa = set(map(int, input().split()))
sb = set(map(int, input().split()))

# XOR ^
print(*sorted(sa ^ sb))
