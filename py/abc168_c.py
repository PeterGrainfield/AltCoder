import math
A, B, H, M = map(int, input().split())

thetaH = (H+M/60)/12*2*math.pi
thetaM = M/60*2*math.pi
c = (A**2 + B**2 - 2*A*B*math.cos(abs(thetaH-thetaM)))**0.5
print(c)
