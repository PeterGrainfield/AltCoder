import itertools


class Direction:
    def __init__(self, oStr, xdif, ydif):
        self.oStr = oStr
        self.xdif = xdif
        self.ydif = ydif


wall = -1  # great wall
up = Direction('U',  0, -1)
down = Direction('D', 0, 1)
right = Direction('R', 1, 0)
left = Direction('L', -1, 0)


def cando(sx, sy, mt, lostTile, d: Direction):
    nx = sx + d.xdif
    ny = sy + d.ydif
    t = mt[ny][nx]
    if t != wall:
        if t not in lostTile:
            return True
    return False


def digging(ans, maxPoint, lostTile, sx, sy):
    retSx = sx
    retSy = sy
    retLostTile = lostTile
    retAns = ans
    retMaxPoint = maxPoint

    directList = itertools.permutations([up, down, right, left])
    for l in directList:
        _sx = sx
        _sy = sy
        _ans = ans
        _point = maxPoint
        _lostTile = lostTile.copy()
        _ans = ans
        mova = True

        cnt = 0
        while mova and cnt < 2:
            mova = False
            cnt += 1
            for d in l:
                if cando(_sx, _sy, mt, _lostTile, d):
                    _sx += d.xdif
                    _sy += d.ydif
                    _ans += d.oStr
                    _point += mp[_sy][_sx]
                    _lostTile.append(mt[_sy][_sx])
                    mova = True
                    break

        if len(_ans) > len(retAns):
            print(_ans, len(_lostTile))
            retAns = _ans
            retMaxPoint = _point
            retLostTile = _lostTile
            retSx, retXy = _sx, _sy

    return retAns, retMaxPoint, retLostTile, retSx, retSy


def initialize():
    xmin, ymin = 1, 1
    xmax, ymax = 50, 50

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
    return sxd, syd, mt, mp


sxd, syd, mt, mp = initialize()


ans = ''
maxPoint = 0
lostTile = [mt[syd][sxd]]
while True:
    _maxPoint = maxPoint
    print(sxd, syd)
    ans, maxPoint, lostTile, sxd, syd,  = digging(
        ans, maxPoint, lostTile, sxd, syd)
    print(maxPoint, _maxPoint)
    if maxPoint == _maxPoint:
        break

print(ans)
