import itertools


class Direction:
    def __init__(self, oStr, xdif, ydif):
        self.oStr = oStr
        self.xdif = xdif
        self.ydif = ydif


def cando(sx, sy, mt, lostTile, d: Direction):
    nx = sx + d.xdif
    ny = sy + d.ydif
    t = mt[ny][nx]
    if t != wall:
        if t not in lostTile:
            return True
    return False


xmin, ymin = 1, 1
xmax, ymax = 50, 50
wall = -1  # great wall
up = Direction('U',  0, -1)
down = Direction('D', 0, 1)
right = Direction('R', 1, 0)
left = Direction('L', -1, 0)
directList = itertools.permutations([up, down, right, left])

sy, sx = map(int, input().split())
sx = sx + 1
sy = sy + 1
sxd = sx
syd = sy
mt = [[wall]*(xmax+2)]
mp = [[wall]*(xmax+2)]
for t in range(xmax):
    lt = list(map(int, input().split()))
    mt.append([wall] + lt[:ymax] + [wall])
for p in range(xmax):
    lp = list(map(int, input().split()))
    mp.append([wall] + lp[:ymax] + [wall])
mt.append([wall]*(xmax+2))
mp.append([wall]*(xmax+2))

ans = ''
maxPoint = 0
for cycle in range(2, 40):
    directList = itertools.permutations([up, down, right, left])
    for lp in directList:
        directList2 = itertools.permutations([up, down, right, left])
        for ls in directList2:
            sx = sxd
            sy = syd
            lostTile = [mt[sy][sx]]
            point = mp[sy][sx]
            mova = True
            path = ''
            dig1 = True
            l = lp
            while mova:
                mova = False
                if len(path) % cycle == cycle - 1:  # ドリル付け替え
                    dig1 = not dig1
                    l = lp if dig1 else ls

                for d in l:
                    if cando(sx, sy, mt, lostTile, d):
                        sx += d.xdif
                        sy += d.ydif
                        path += d.oStr
                        point += mp[sy][sx]
                        lostTile.append(mt[sy][sx])
                        mova = True
                        break
            ans = path if point > maxPoint else ans
            maxPoint = max(point, maxPoint)


print(ans)
