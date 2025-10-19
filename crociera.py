import csv
from Passeggeri import passeggeri
from Cabina import Cabina, CabinaAnimali, CabinaDeluxe

#definisco la classe crocera
class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.lista_passeggeri = []
        self.listaCabine = []
        self.assegnazioneCabine = {}
        self.elenco_pass = {}


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as dati_passeggeri:
                lettura_dati = csv.reader(dati_passeggeri, delimiter=',')
                for row in lettura_dati:
                    if row[0].startswith('P'): # se la prima casella del file inizia con P, tratta i dati successivi della riga come dati del passegero e inserira i dati nella classe passeggero
                        CodPasseggeri = row[0]
                        Nome = row[1]
                        Cognome = row[2]
                        passeggero = passeggeri(CodPasseggeri, Nome, Cognome)
                        self.lista_passeggeri.append(passeggero)
                    elif row[0].startswith('C'): # se il codice inizia con C trattera i dati della riga come quelli di una cabina e la inserira nella classe cabina
                        CodCabina = row[0]
                        letti = int(row[1])
                        ponte = int(row[2])
                        prezzoBase = int(row[3])

                        try:

                            if row[4].isdigit():  # controlla se la stringa è un numero, ne consegue i dati verranno insieriti nella classe cabina animali
                                numAnimali = int(row[4])
                                cab_animali = CabinaAnimali(CodCabina, letti, ponte, prezzoBase, numAnimali)

                                self.listaCabine.append(cab_animali)

                            else: # se non è cabina animali sarà quella deluxe e la trattera come tale inserendola nella classe cabina deluxe
                                stile_cabina = row[4].strip()
                                cabDeluxe = CabinaDeluxe(CodCabina, letti, ponte, prezzoBase, stile_cabina)
                                cabDeluxe.prezzoBase = cabDeluxe.maggiorazionePrezzo()
                                self.listaCabine.append(cabDeluxe)
                        except IndexError:# se da errore sugli indici vuol dire che non e ne cabanimali ne cabdeluxe, di conseguenza verra trattata da cabina base
                            cab = Cabina(CodCabina, letti, ponte, prezzoBase)
                            self.listaCabine.append(cab)


            return self.lista_passeggeri, self.listaCabine
        except FileNotFoundError: # gestione errore se il file non è stato trovato
            print("File non trovato")





    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        CabinaDaTrovare: Cabina = None  #inizializzo cabinia e passeggero da trovare come none
        PasseggeriDaTrovare = None
        for c in self.listaCabine:
            if c.codCabina == codice_cabina:
                CabinaDaTrovare = c  # condizione che verifica se la cabina esiste
                break
        if CabinaDaTrovare is None:
            raise Exception("Cabina inesistente") # solleva un errore se la cabina non esiste
        for p in self.lista_passeggeri:
            if p.CodPasseggeri == codice_passeggero: #condizione che verifica se il passeggero esiste
                PasseggeriDaTrovare = p
                break
        if PasseggeriDaTrovare is None:
            raise Exception("Passeggeri inesistente") # solleva un errore se il passeggero non esiste
        if CabinaDaTrovare.disponibilita is True: # verifica se la cabina è disponibile
            agg_disp = CabinaDaTrovare.gest_disponibilita() # metodo della classe che aggiorna la disponibilità della cabina
            if codice_passeggero not in self.assegnazioneCabine.keys():# verifica che il passeggero non sia stato ancora  abbianto a nessuna cabina
                self.assegnazioneCabine[codice_passeggero] = CabinaDaTrovare.codCabina # aggiunge il passeggero con la sua cabina all'elenco
            else:
                raise Exception("Passeggero gia assegnato") #solleva un errore se il pass è gia stato abbinato

        else:
            raise Exception("Cabina occupata") # solleva errore se la cabina è occupata
        return self.assegnazioneCabine



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.listaCabine, key=lambda cab: cab.prezzoBase, reverse=True)# ordina le cabine per prezzo in ordine decrescente


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passe in self.lista_passeggeri:
            codice  = passe.CodPasseggeri
            cabina = self.assegnazioneCabine.get(codice, "Non assegnato")# metodo get che se il codice esiste mi restituisce la cabina a cui è stato assegnato, se non esiste ritorna non assegnato
            self.assegnazioneCabine[codice] = cabina
        return self.assegnazioneCabine





