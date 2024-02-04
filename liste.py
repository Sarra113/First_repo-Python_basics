fructe = ['mar', 'banana', 'portocala', 3, 3, True]
# declarare lista cu valori
# listele in py pot sa cuprinda elemente de tipuri diferite
# si au dimentiuse dinamica

print(fructe)

#accesam un elem in functie de index

print(fructe[1])

# adaugare element
fructe.append('rosie')

# suprascriere
fructe[0] = ('para')
print(fructe)

print(len(fructe))

# scoate si ne returneaza ultimul elem
last = fructe.pop()

print('ultimul element:', last)
print('lista ', fructe)

# de cate ori apare elem
print(fructe.count(3))

fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)