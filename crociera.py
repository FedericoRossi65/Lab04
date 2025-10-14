import csv
from Passeggeri import passeggeri
from Cabina import Cabina, CabinaAnimali, CabinaDeluxe


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.lista_passeggeri = []
        self.listaCabine = []


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
                        Cognome = [2]
                        passeggero = passeggeri(CodPasseggeri, Nome, Cognome)
                        self.lista_passeggeri.append(passeggero)
                    elif row[0].startswith('C'):
                        CodCabina = row[0]
                        letti = int(row[1])
                        ponte = int(row[2])
                        prezzoBase = float(row[3])
                        if row[4] is int:
                            numAnimali = int(row[4])

                            cab_animali = CabinaAnimali(CodCabina,letti,ponte,prezzoBase, numAnimali)
                            self.listaCabine.append(cab_animali)
                        else:
                            stile_cabina = row[4]
                            cabDeluxe = CabinaDeluxe(CodCabina,letti,ponte,prezzoBase, stile_cabina)
                            self.listaCabine.append(cabDeluxe)
                return self.lista_passeggeri, self.listaCabine
        except FileNotFoundError:
            print("File non trovato")
        except Exception:
            print("Errore anomalo")




    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # T


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO



