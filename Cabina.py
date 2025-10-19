class Cabina: # definisco la classe padre cabina con i suoi attributi
    def __init__(self,codCabina,letti,ponte,prezzoBase,disponibilita = True):
        self.codCabina = codCabina
        self.letti = letti
        self.ponte = ponte
        self.prezzoBase = prezzoBase
        self.disponibilita = disponibilita
    #metodo che mi aggiorna la disponibilita quandi viene chiamato
    def gest_disponibilita(self):
        self.disponibilita = False
        return self.disponibilita
    #metodo str per avere la stampa desiderata
    def __str__(self):
        if self.disponibilita==True: # condizione che converte i valori booleani in stringa
            stato = 'Disponibile'
        else:
            stato = 'Non disponibile'
        return f'{self.codCabina}: Cabina Base - {self.letti} letti - Prezzo {self.prezzoBase}€  - {stato}'

    __repr__ = __str__
#definisco la prima classe figlia di cabina
class CabinaAnimali(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,numAnimali):
        super().__init__(codCabina,letti,ponte,prezzoBase)
        self.numAnimali = numAnimali

    #metodo che mi aggiorna il prezzo
    def maggiorazionePrezzo(self):
        'prezzo finale = prezzo base × (1 + 0.10 × max_animali)'
        prezzoMaggiorato = round(self.prezzoBase*(1+(0.10*self.numAnimali)),2)

        return prezzoMaggiorato
    # CAB6: Animali | 4 letti - Ponte 1 - Prezzo 234.00€ - Max animali: 3 – Disponibile
    def __str__(self):
        if self.disponibilita==True:
            stato = 'Disponibile'
        else:
            stato = 'Non disponibile'
        return f'{self.codCabina}: Animali | {self.letti} letti - Ponte {self.ponte} - Prezzo {CabinaAnimali.maggiorazionePrezzo(self)}€  - {stato}'

    __repr__ = __str__
# definisco la seconda classe figlia di cabina
class CabinaDeluxe(Cabina):
    def __init__(self,codCabina,letti,ponte,prezzoBase,Stile):
        super().__init__(codCabina,letti,ponte,prezzoBase)
        self.Stile = Stile
#maggiorazione del prezzo come la classe prima
    def maggiorazionePrezzo(self):
        'prezzo finale = prezzo base × 1.20'
        prezzoMaggiorato = round((self.prezzoBase*1.20),2)

        return prezzoMaggiorato
    def __str__(self):
        if self.disponibilita==True:
            stato = 'Disponibile'
        else:
            stato = 'Non disponibile'
        return f'{self.codCabina}: {self.Stile} | {self.letti} letti -  Prezzo: {CabinaDeluxe.maggiorazionePrezzo(self)}€  - {stato} '

    __repr__ = __str__