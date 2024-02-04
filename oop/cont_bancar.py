class ContBancar:
    #constructor; zona de atribute definita prin constructor
    # ~ variabilele

    def __init__(self, titularCont, iban):  # self este clasa
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # metodele ~ functiile
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print(f'-----------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('PIN gresit')
            self.incercari_activare = self.incercari_activare + 1
           # self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.sold += suma # se ia suma si se adauga la sold
        self.salut()
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma): #suma de aici nu e aceesi cu cea de mai sus. ea traieste doar in metoda asta
        #variable scope
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')



    def salut(self):
        print(f'Buna {self.titularCont}')

