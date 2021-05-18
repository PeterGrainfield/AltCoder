S = input()

print("Yes" if not ('E' in S)^('W' in S) and not ('N' in S)^('S' in S) else "No")
