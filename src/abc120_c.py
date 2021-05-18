# 1 <= N <= 10**5
S = input()

cntRed = 0
cntBlue = 0
boom = 0
for i in range(len(S)):
    # print(cntRed, cntBlue, boom)
    if S[i] == "0":  # red
        if cntBlue > 0:
            cntBlue -= 1
            boom += 1
        else:
            cntRed += 1
    else:  # blue
        if cntRed > 0:
            cntRed -= 1
            boom += 1
        else:
            cntBlue += 1

print(boom * 2)
