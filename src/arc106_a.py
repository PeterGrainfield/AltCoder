N = int(input())

for n3 in range(1, 38):
    for n5 in range(1, 26):
        if 3**n3+5**n5 ==N:
            print(n3, n5)
            exit()
print(-1)
