class passeggeri:
    def __init__(self,CodPasseggeri,Nome,Cognome):
        self.CodPasseggeri = CodPasseggeri
        self.Nome = Nome
        self.Cognome = Cognome
    def __str__(self):
        return f'{self.CodPasseggeri} - Nome: {self.Nome} - Cognome: {self.Cognome}'

    __repr__ = __str__