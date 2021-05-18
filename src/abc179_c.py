N = int(input())

case = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        if N > a * b:
            print(a, b)
            case += 1
        else:
            break

print(case)
