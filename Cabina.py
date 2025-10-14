class Cabina:
    def __init__(self,codCabina,letti,ponte,prezzoBase):
        self.codCabina = codCabina
        self.letti = letti
        self.ponte = ponte
        self.prezzoBase = prezzoBase
class CabinaAnimali(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,numAnimali):
        super().__init__(codCabina,letti,ponte,prezzoBase)
        self.numAnimali = numAnimali

    def maggiorazionePrezzo(self):
        'prezzo finale = prezzo base × (1 + 0.10 × max_animali)'
        self.prezzoBase += self.prezzoBase*(1+0.10*self.numAnimali)

        return self.prezzoBase
class CabinaDeluxe(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,Stile):
        super().__init__(codCabina,letti,ponte,prezzoBase)
        self.Stile = Stile
    def maggioramentoPrezzo(self):
        'prezzo finale = prezzo base × 1.20'
        self.prezzoBase += self.prezzoBase*1.20
        return self.prezzoBase
