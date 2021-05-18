N = int(input())

s = set()
for i in range(2, int(N**0.5)+1):
    a = i * i
    while a <= N:
        s.add(a)
        a *= i
print(N-len(s))