N = int(input())
la = list(map(int, input().split()))
lb = list(map(int, input().split())) + [0]

# print(la, lb)

bustard = 0
for i in range(N+1):
    if i > 0:
        k = min(la[i], lb[i-1])
        bustard += k
        la[i] -= k

    j = min(la[i], lb[i])
    bustard += j
    la[i] -= j
    lb[i] -= j

print(bustard)
