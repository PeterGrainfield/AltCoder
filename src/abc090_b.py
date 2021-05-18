A, B = map(int, input().split())

cnt = 0
for n in range(A, B + 1):
    strn = str(n)
    # print(strn, strn[::-1])
    if strn == strn[::-1]:
        cnt += 1
print(cnt)
