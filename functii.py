def printGreeting():
    print('Buna ziua!Bine ati venit')

def printGreetingByName(nume, prenume): # params
    print(f'Buna ziua {nume} {prenume}!')

def mediaNr(a, b,c):
    return (a + b + c) / 3

def piValue():
    return 3.14
    print('abc') #nu se executa. return e ultima instructiune pt functie

# excercitiu
# daca persoana e majora returnati true, altfel false
def verificare_major(varsta): #varsta o vedem la apelare. params
    if varsta >= 18:
        return True
    else:
        return False
# situatie cu 2 return dar de fapt doar una poate exista odata - intr-un prezent


# zona de apelare (desktop)
printGreeting()
printGreeting()

printGreetingByName('Creta', 'Sarra')
printGreetingByName('Pop', 'Ana')
print(mediaNr(3, 3, 4))
print(piValue())
print(verificare_major(19))
print(verificare_major(17))

age = int(input('introduceti varsta')) # il obliga sa fie int. by default ar fi string
if verificare_major(age):
    print('Cont creat')
else:
    print('Nu ai varsta minima necesara')