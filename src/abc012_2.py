N = int(input())

hour, sp = divmod(N, 3600)
minute, sp = divmod(sp, 60)

print("{:02}:{:02}:{:02}".format(hour, minute, sp))
