ln = list(map(int, input().split()))
ln.sort(reverse=True)

print(ln[0]*10+ln[1]+ln[2])
