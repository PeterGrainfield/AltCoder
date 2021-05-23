c = [list(input())[::-1] for _ in range(3)]
d = {'a': c[0], 'b': c[1], 'c': c[2]}
turn = 'a'
while len(d[turn]):
    turn = d[turn].pop()

print(turn.upper())
