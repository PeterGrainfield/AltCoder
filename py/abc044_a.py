N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N > K:
    print(X*K+(N-K)*Y)
else:
    print(N*X)