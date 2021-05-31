N, L = map(int,input().split())
S = input()

cnt = 1
crash = 0
for c in S:
    if c == "+":
        cnt+=1
    else:
        cnt-=1
    if cnt > L:
        crash += 1
        cnt = 1
print(crash)