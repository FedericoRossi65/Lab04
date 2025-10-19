from crociera import Crociera

def menu():
    print(f'\n--- MENU CROCIERA ---')
    print("1. Modifica nome della crociera")
    print("2. Carica dati da file")
    print("3. Assegna cabina a passeggero")
    print("4. Visualizza cabine ordinate per prezzo")
    print("5. Visualizza elenco passeggeri")
    print("6. Esci")

    return input("Scegli un'opzione >> ")

def main():
    crociera = Crociera("MSC Futura")

    while True:
        scelta = menu()

        if scelta == "1": # aggiorna il nome del ìla crocera
            nuovo_nome = input("Inserisci il nuovo nome della crociera: ")

            crociera.nome = nuovo_nome
            print(f'Il nuovo nome della crocera è {nuovo_nome}')

        elif scelta == "2": # carica i dati del file
            file_path = "dati_crociera.csv"
            try:
                dati = crociera.carica_file_dati(file_path)




                print("Dati caricati correttamente.")
            except FileNotFoundError:
                print("File non trovato.")
        # assegnazione passeggero|cabina
        elif scelta == "3":
            codice_cabina = input("Codice cabina: ")
            codice_passeggero = input("Codice passeggero: ")
            try:
                ass = (crociera.assegna_passeggero_a_cabina(codice_cabina, codice_passeggero))
                for c,v in ass.items(): # ciclo per il print desisderato
                    print(f'{c} | {v}')
                print("Cabina assegnata con successo.")
            except Exception as e:
                print(f"Errore: {e}")

        elif scelta == "4": # ordina le cabine in base al prezzp
            cabine_ordinate = crociera.cabine_ordinate_per_prezzo()
            print("\n--- Cabine ordinate per prezzo ---")
            for c in cabine_ordinate:
                print(c)

        elif scelta == "5":
            print("\n--- Elenco passeggeri ---")
            e = (crociera.elenca_passeggeri())
            for p,d in e.items(): # ciclo  per avere il print desiderato
                print(f'{p} | {d}')

        elif scelta == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()