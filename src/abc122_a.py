b = input()

acgt = {"A": "T", "C": "G", "G": "C", "T": "A"}
ans = ""
for c in b:
    ans += acgt[c]

print(ans)
