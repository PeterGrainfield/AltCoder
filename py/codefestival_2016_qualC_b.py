K, T = map(int, input().split())
la = list(map(int, input().split()))
amax = max(la)
print(max(amax-1-(K-amax),0))

