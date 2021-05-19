H, W = map(int, input().split())

wall = '#'
print(wall*(W+2))
for i in range(H):
    print(wall + input() + wall)
print(wall*(W+2))
