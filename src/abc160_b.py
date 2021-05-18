X = int(input())

fiveh, remain = divmod(X, 500)
fcoin = remain // 5

print(fiveh * 1000 + fcoin * 5)
