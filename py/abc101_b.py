S = input()
Ni = int(S)
Nl = sum(list(map(int, S)))
if Ni % Nl == 0:
    print("Yes")
else:
    print("No")
    