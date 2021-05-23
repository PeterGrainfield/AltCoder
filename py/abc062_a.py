ls = list(map(str,input().split()))

ans = ""
for word in ls:
    word[0] = word[0].upper()
    ans+=word
print(ans)