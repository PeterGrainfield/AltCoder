dayofw = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")

S = input()
for i in range(7):
    if dayofw[i] == S:
        print(7-i)
