import collections
N = int(input())
S = list(map(int, input()))
T = list(map(int, input()))

sc = collections.Counter(S)
st = collections.Counter(T)
if sc[0] != st[0]:
    print(-1)
    exit()

ans = 0
for i in range(N):
    cnt = 0
    if S[i] != T[i]:
        # 0の時は1までに必要な0の数
        if S[i] == 0:
            for j in range(i+1, N):
                if S[j] == 1:
                    cnt += 1
                    S[i], S[j] = S[j], S[i]
                    break
                cnt += 1
        else:  # 1の時はT=1 S=0となっているところまでの0の数
            for j in range(i+1, N):
                if S[j] == 0 and T[j] == 1:
                    cnt += 1
                    S[i], S[j] = S[j], S[i]
                    break
                if S[j] == 0 and T[j] == 0:
                    cnt += 1
        ans += cnt
        ###
        # print(S, T)
        ###
print(ans)
