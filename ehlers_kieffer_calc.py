import math

Vs = 3.97
Vp = 8.06
Vmax = 4.87
Vol = 130.5
Z = 2

u2 = (2/(Vs**(-3) + Vmax**(-3)))**(1/3)
u1 = (1/(2*(Vs**(-3)) - u2**(-3)))**(1/3)
u3 = Vp

# print(u2)
# print(u1)
# print(u3)

acoustic_array = [u1, u2, u3]

print(acoustic_array)

Vmol = Vol*0.6023/Z

print('Molar volume of zircon is: ', Vmol)

Kmax = (6*(math.pi)*(math.pi)*(10**24)/Vol)**1/3

print(Kmax)