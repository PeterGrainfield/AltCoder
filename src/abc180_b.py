N = int(input())
lx = list(map(int, input().split()))

manh = 0
euq = 0
scheb = 0
labsx = []
for x in lx:
    manh += abs(x)
    euq += abs(x)**2
    scheb = max(scheb, abs(x))

print(manh)
print(euq**0.5)
print(scheb)
