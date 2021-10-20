class Spørsmål:
    def __init__(self, spørsmål, alternativer, riktig_svar):
        self.spørsmål = spørsmål
        self.alternativer = alternativer
        self.riktig_svar = riktig_svar
    
    def __str__(self):
        alternativer = []
        for i in range(len(self.alternativer)):
            alternativer.append(str(i+1) + ": " + self.alternativer[i])
        return self.spørsmål + "\n" + str(alternativer)

    def sjekk_svar(self):
        avgitt_svar = int(input())
        if avgitt_svar == self.riktig_svar:
            return 1
        else:
            return 0


spm1 = Spørsmål("Hvordan by er en hovedstad?", ("Stavanger", "Harstad", "Oslo"), 3)
spm2 = Spørsmål("Hvilke tall er minst?", ("4", "5", "6"), 1)
spm3 = Spørsmål("Hvilke passer ikke inn?", ("Ja", "Nei", "Kanskje", "Hade"), 4)
spm4 = Spørsmål("Hvilke passer ikke inn?", ("Ja", "Nei", "Kanskje", "Hade"), 4)


spm = [spm1, spm2, spm3, spm4] 



def spill():
    poeng = 0
    full_score = len(spm)   
    for i in range(len(spm)):
        print(spm[i])
        if spm[i].sjekk_svar() == 1:
            poeng += 1
        print("\n")
    print(f"Du fikk {poeng}/{full_score} riktige")


if __name__ == '__main__':
    spill()

        