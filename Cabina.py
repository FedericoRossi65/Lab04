class Cabina:
    def __init__(self,codCabina,letti,ponte,prezzoBase,disponibilita):
        self.codCabina = codCabina
        self.letti = letti
        self.ponte = ponte
        self.prezzoBase = prezzoBase
        self.disponibilita = disponibilita
    def __str__(self):
        return f'{self.codCabina}: Cabina Base - {self.letti} letti - Prezzo {self.prezzoBase} - {self.disponibilita}'

    __repr__ = __str__
class CabinaAnimali(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,numAnimali,disponibilita):
        super().__init__(codCabina,letti,ponte,prezzoBase,disponibilita)
        self.numAnimali = numAnimali


    def maggiorazionePrezzo(self):
        'prezzo finale = prezzo base × (1 + 0.10 × max_animali)'
        self.prezzoBase *= (1+0.10*self.numAnimali)

        return self.prezzoBase
    # CAB6: Animali | 4 letti - Ponte 1 - Prezzo 234.00€ - Max animali: 3 – Disponibile
    def __str__(self):
        return f'{self.codCabina}: Animali | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzoBase} - {self.disponibilita}'

    __repr__ = __str__
class CabinaDeluxe(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,Stile,disponibilita):
        super().__init__(codCabina,letti,ponte,prezzoBase,disponibilita)
        self.Stile = Stile
    def maggioramentoPrezzo(self):
        'prezzo finale = prezzo base × 1.20'
        self.prezzoBase *= 1.20
        return self.prezzoBase
    def __str__(self):
        return f'{self.codCabina}: {self.Stile} | {self.letti} letti - Prezzo {self.prezzoBase} - Prezzo: {self.prezzoBase} - {self.disponibilita}'

    __repr__ = __str__
