N = int(input())
la = list(map(int, input().split()))

minCost = 100*(200**2)
for y in range(-100, 101):
    cost = 0
    for a in la:
        cost += (a-y)**2
    minCost = min(minCost, cost)

print(minCost)
