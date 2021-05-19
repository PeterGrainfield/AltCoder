S = input()

cnt = 0
word = ""
preword = ""
for c in S:
    word += c
    if word != preword:
        cnt += 1
        preword = word
        word = ""
        # print(preword + ',')
print(cnt)
