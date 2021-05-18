N = int(input())
lp = [int(input()) for _ in range(N)]

print(sum(lp)-max(lp)//2)