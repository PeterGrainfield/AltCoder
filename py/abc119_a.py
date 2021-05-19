S = input()

if int(S[0:4]) > 2019:
    print("TBD")
elif int(S[0:4]) == 2019 and int(S[5:7]) > 4:
    print("TBD")
else:
    print("Heisei")
