H = int(input())
W = int(input())
N = int(input())

painted = 0
cnt = 0
while painted < N:
    if H >= W:
        painted += H
        W -= 1
    else:
        painted += W
        H -= 1
    cnt += 1
print(cnt)
