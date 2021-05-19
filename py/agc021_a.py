N = int(input())
strN = str(N)
_ans = 0
if N < 10:
    _ans = N
elif strN[0] == "1":
    _ans = int("9"*(len(strN)-1))
else:
    _ans = int(str(int(strN[0])-1) + "9"*(len(strN)-1))
ans = sum(int(x) for x in str(_ans))
if N >= 10:
    for i in range(N, N-10, -1):
        sumD = sum(int(x) for x in str(i))
        ans = max(ans, sumD)
print(ans)
