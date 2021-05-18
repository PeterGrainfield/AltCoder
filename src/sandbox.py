
import itertools
happo = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
print(happo)
happo2 = [i for i in itertools.product((-1, 0, 1), repeat=2)]
happo2.remove((0, 0))
print(happo2)
