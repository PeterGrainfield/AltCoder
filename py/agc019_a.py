Q, H, S, D = map(int, input().split())
N = int(input())

cost = min(Q*4, H*2, S)
price = 0
if D / 2 < cost:
    afford = N // 2
    price += D * afford
    N -= afford * 2

price += N * cost
print(int(price))
