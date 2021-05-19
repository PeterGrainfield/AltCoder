N = int(input())
la = list(map(int, input().split()))

ansr = 0
for a in la:
    ansr += 1/a

print(1/ansr)
