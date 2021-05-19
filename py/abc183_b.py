sx, sy, gx, gy = map(int, input().split())

dx = sx - gx
dy = sy + gy

x = sx - (sy * dx / dy) 
print(x)
