N = 610

ans = ""
for i in range(N):
    ans += input().replace("AC", "")
    if i % 10 == 9:
        ans += "\n"
    else:
        ans += ","
print(ans)
