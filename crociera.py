import csv
from Passeggeri import passeggeri
from Cabina import Cabina, CabinaAnimali, CabinaDeluxe


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.lista_passeggeri = []
        self.listaCabine = []
        self.assegnazioneCabine = {}



    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as dati_passeggeri:
                lettura_dati = csv.reader(dati_passeggeri, delimiter=',')
                for row in lettura_dati:
                    if row[0].startswith('P'):
                        CodPasseggeri = row[0]
                        Nome = row[1]
                        Cognome = row[2]
                        passeggero = passeggeri(CodPasseggeri, Nome, Cognome)
                        self.lista_passeggeri.append(passeggero)
                    elif row[0].startswith('C'):
                        CodCabina = row[0]
                        letti = int(row[1])
                        ponte = int(row[2])
                        prezzoBase = int(row[3])

                        try:

                            if row[4].isdigit():  # controlla se la stringa è un numero
                                numAnimali = int(row[4])
                                cab_animali = CabinaAnimali(CodCabina, letti, ponte, prezzoBase, numAnimali)

                                self.listaCabine.append(cab_animali)

                            else:
                                stile_cabina = row[4].strip()
                                cabDeluxe = CabinaDeluxe(CodCabina, letti, ponte, prezzoBase, stile_cabina)
                                cabDeluxe.prezzoBase = cabDeluxe.maggiorazionePrezzo()
                                self.listaCabine.append(cabDeluxe)
                        except IndexError:
                            cab = Cabina(CodCabina, letti, ponte, prezzoBase)
                            self.listaCabine.append(cab)


            return self.lista_passeggeri, self.listaCabine
        except FileNotFoundError:
            print("File non trovato")





    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        CabinaDaTrovare: Cabina = None
        PasseggeriDaTrovare = None
        for c in self.listaCabine:
            if c.codCabina == codice_cabina:
                CabinaDaTrovare = c
                break
        if CabinaDaTrovare is None:
            raise Exception("Cabina inesistente")
        for p in self.lista_passeggeri:
            if p.CodPasseggeri == codice_passeggero:
                PasseggeriDaTrovare = p
                break
        if PasseggeriDaTrovare is None:
            raise Exception("Passeggeri inesistente")
        if CabinaDaTrovare.disponibilita is True:
            agg_disp = CabinaDaTrovare.gest_disponibilita()
            if codice_passeggero not in self.assegnazioneCabine.keys():
                self.assegnazioneCabine[codice_passeggero] = CabinaDaTrovare
            else:
                raise Exception("Passeggero gia assegnato")

        else:
            raise Exception("Cabina occupata")
        return f"Cabina {codice_cabina} assegnata a passeggero {codice_passeggero}."







    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.listaCabine, key=lambda cab: cab.prezzoBase, reverse=True)


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

