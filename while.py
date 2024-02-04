# masina merge cat timp inca are benzina

litri_benzina = 10
while litri_benzina > 0:  # cand intram cu -1 conditia este falsa si nu mai intram in while, next este printstop
    # acceleram
    print('Vrum Vrum!')
    # scadem benzina - fosta valoare -1
    # scadem cate 1l benzina la fiecare accelerare
    litri_benzina = litri_benzina - 1 # 9 litri etc
    # aprindem bec cand avem mai mic sau egal de 3l
    if litri_benzina <= 3:
        print('beculetul rosu')
print('stop!')

...