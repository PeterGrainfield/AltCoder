H1, M1, H2, M2, K = map(int, input().split())
t1, t2 = H1*60 + M1, H2*60+M2

print(t2-t1-K)
