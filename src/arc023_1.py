y = int(input())
m = int(input())
d = int(input())

day0 = 735369

if m < 3:
    y -= 1
    m += 12

days = 365*y + (y//4) - (y//100) + (y//400) + (306*(m+1)//10) + d - 429

print(day0 - days)
