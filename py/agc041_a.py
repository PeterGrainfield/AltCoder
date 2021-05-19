N, A, B = map(int, input().split())

move = 0
if (B - A) % 2 == 0:
    move = (B-A) // 2
else:
    move = min(A-1, N-B) + 1 + (B-A-1) // 2
print(int(move))
