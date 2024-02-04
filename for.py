# problema dalmatini. returneaza de la 1 la 101

# for i in range(1, 102):
#     print(f'Dalmatianul cu nr {i}')

# dalmatienii din 2 in 2
for i in range(1, 102, 2): #nu vedem 102 pt ca indexul incepe de la 0 nu 1
    print(f'Dalmatianul cu nr {i}')

# parcurgere lista cu for prin intermediul indexului
numere = [3, 7, 10, 20, 30]
print(len(numere))

for i in range(0, len(numere)):
    print(f'indexul curent este {i}')
    print(f'numarul curent este  {numere[i]}')


# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'suma este {s}')


list = ['mar', 'bananna', 'para']
for x in ('bananna'):
    print(x)