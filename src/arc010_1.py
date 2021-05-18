N, M, A, B = map(int, input().split())

lc = [int(input()) for _ in range(M)]

card = N
for i, c in enumerate(lc):
    if card <= A:
        card += B
    card -= c
    if card < 0:
        print(i+1)
        break
else:
    print("complete")
