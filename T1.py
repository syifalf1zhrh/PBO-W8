from collections import namedtuple

Koordinat = namedtuple('Koodinat',['x', 'y'])
titik1=Koordinat(2, 4)

#akses elemen dengan indeks
print("X :", titik1[0])

#akses elemen dengan nama atribut
print("Y :", titik1.y)

#akses elemen dengan getattr
print("X :", getattr(titik1, 'x'))


