
piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')


# if else
# daca nr e par printam acest lucru
# altfel, printam impar

nr = 3
# ce inseamna par? se imparte exact la 2
# daca se imparte exact la 2 impartirea da restul 0

if nr % 2 == 0:
    print('par')
else:
    print('impar')

if (nr > 0):
    print('pozitiv')
else:
    print('nr nu e pozitiv')

#if, else, if, else
#cum saluta robotul in fct de ora
#luam date de la tastatura
#ne asig ca sunt transformate din strinn in int

# ora = int(input('Introdu ora'))
# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('buna dimi')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora mai mare decat 24')

# robotel telefonic
optiunea = int(input('Alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales ro')
elif optiunea == 2:
    print('ati ales eng')
else:
    print('nu am idetificat optiunea, try again')