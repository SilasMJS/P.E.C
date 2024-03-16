#import math
PI = 3.141592
raio = float(input())
circ = 2 * PI * raio
a_circ = PI * raio ** 2
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4 / 3 * PI * raio ** 3
print(f'{circ:.6f}\n{a_circ:.6f}\n{a_esfera:.6f}\n{vol_esfera:.6f}')
