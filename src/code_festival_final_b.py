ln = list(map(int, input()))

plus = True
ans = 0
for n in ln:
    if plus:
        ans += n
    else:
        ans -= n
    plus = not plus
print(ans)
