K, A, B = map(int, input().split())

n1 = K+1
if B - A < 2 or K < A-1+1:
    print(n1)
else:
    n2 = A
    K -= A - 1
    n2 += K//2*(B-A)
    if K % 2 == 1:
        n2 += 1
    print(max(n1,n2))
