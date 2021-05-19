# 0 <= A, B, C, D <=9
A, B, C, D = [int(c) for c in input()]

for i in range(1, -2, -2):
    for j in range(1, -2, -2):
        for k in range(1, -2, -2):
            ans = A + B * i + C * j + D * k
            if ans == 7:
                op1 = '+' if i == 1 else "-"
                op2 = '+' if j == 1 else "-"
                op3 = '+' if k == 1 else "-"
                print(str(A) + op1 + str(B) + op2 +
                      str(C) + op3 + str(D) + "=7")
                exit()
