N = int(input())

X = sum(map(int, str(N)))
if N%X==0:
    print("Yes")
else:
    print("No")