'''n = int(input())
m = int(input())

char= '*'
i=0
print ((char + " ")*m)
while i < n-2:
    print (char +char)
    i+= 1

if n>1:
    print ((char+" ")*m)
'''
'''
3 altura
4 base

* * * *
**



'''

'''n= int(input())

if n<9:
    print('1 ' *n)
    for i in range(1, n):
        t= i+1
        j= n-i
        print(' '*i + (str(t)+ ' ')*j)
'''

'''a = int(input())

b = a + 11
c= (b%11)
d= b - c

print(d)'''
'''
n = int(input())
a =0
for i in range(n, 0):
    a += i

print(a)
'''

import random

lista = [('Polígono regular', 'Perímetro: n*l Area: p*ap Volumen: a*h'),
         ('Tetraedro', '(a = una de las aristas) Área T: _⁄3*a3  Volumen: a3212'),
         ('Hexaedro', '(a = una de las aristas) Área L: 4a2 Área T: 6a2 Volumen: a3'),
         ('Octaedro', 'Área T: 23 a3 Volumen a323'),
         ('Prisma', '(usa las fórmulas de polígono regular) Área L: perímetro b*h Área T: AL + 2Ab Volumen: Ab * h'),
         ('Pirámide:','Área L.: (perímetro b * apotema)/2 Área T.: AL + AB Volumen: (Ab*h)/3'),
         ('Tronco de pirámide','Área L.: P + p2*Ap Área T.: AB + Ab +AL Volumen: h3*(AB+Ab+AB*Ab)'),
         ('Esfera:', 'Perímetro (círculo): 2π*r Área: 4π*r² Volumen: (4π*r3)/3'),
         ('Cilindro', 'Area L.: 2π*r*h Área T: 2π*r*h + 2π*r2 Volumen: π*r2* h'),
         ('Cono', 'Área B: π*r2 Area L.: π*r*g Área T: AL + AB Volumen: (AB*h)/3'),
         ('Tronco de Cono', 'Área bases: π*r2 Area L:π*(r1 + r2)*g Área T: AL + AB + Ab Volumen: 1/3π*h*(r12+r22+r1+r2))]')]

while input('Otro? [S/N]: ')  == 'S':
    for a in lista:
        for i in a:
            print(i)
            input('Siguiente')