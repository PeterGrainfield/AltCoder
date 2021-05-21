N, K = map(int, input().split())
listL = list(map(int, input().split()))
listL.sort(reverse=True)

print(sum(listL[:min(K, len(listL))]))
