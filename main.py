import os
import sys

class Spiller:
    def __init__(self, nummer, poeng):
        self.nummer = nummer
        self.poeng = poeng
    def __str__(self):
        return f"Spiller {self.nummer} fikk {self.poeng} poeng"
        
        

class Spørsmål: 
    def __init__(self, spørsmål, alternativer, riktig_svar):
        self.spørsmål = spørsmål
        self.alternativer = alternativer
        self.riktig_svar = riktig_svar
    
    def __str__(self):
        alternativer = []
        for i in range(len(self.alternativer)):
            alternativer.append(str(i+1) + ": " + self.alternativer[i])
        return self.spørsmål + "\n" + str(alternativer) + "\n"

    def sjekk_svar(self):
        avgitt_svar = int(input())
        riktig_svar = int(self.riktig_svar)
        if avgitt_svar == (riktig_svar+1):                                          #Bruker riktig_svar +1 fordi jeg vil at brukeren skal svare med spm nummeret ikke index
            return 1
        else:
            return 0
    
    
    def korrekt_svar_tekst(self):
        alternativer = []
        for i in range(len(self.alternativer)):
            alternativer.append(self.alternativer[i])
        return alternativer[int(self.riktig_svar)]

spillere = []
def create_players():
    antall_spillere = int(input("Hvor mange spillere?\n"))
    for i in range(1, antall_spillere+1):
        spillere.append(Spiller(i, 0))
    

questions = []                                                                      #Listen som vil inneholde alle spørsmålene etter create_questions() har kjørt

def create_questions():
    fila = (open(os.path.join(sys.path[0], "sporsmaalsfil.txt"), "r"))              #Åpner filen
    fil = [] 
    for linje in fila:                                                              #Splitter filen opp i linjer siden det er 1 spørsmål for hver linje
        fil.append(linje)
        alternativer = []
    for i in range(len(fil)):                                                       #Tar for meg en og en linje
        rad = fil[i].split(":")                                                     #Splitter linjen opp med seperatoren :
        alternativer = rad[2].strip().strip("[").strip("]").split(",")              
        questions.append(Spørsmål(rad[0], alternativer, rad[1]))                    #Bruker klassen Spørsmål og sender de ferdige spørsmålene inn i listen questions

def spill():                                                                        #Funksjonen som kjører selve spillet
    full_score = len(questions)
    for i in range(full_score):
        print(questions[i])
        spm_nr = i
        svar = []
        for i in range(len(spillere)):
            spiller = i
            print(f"Spiller {i+1}:")
            if questions[spm_nr].sjekk_svar() == 1:
                spillere[i].poeng += 1
                svar.append("riktig")
            else:
                svar.append("feil")
        print(f"Riktig svar:{questions[spm_nr].korrekt_svar_tekst()} \n")
        for i in range(len(spillere)):
            print(f"Spiller {i+1} fikk {svar[i]}")
        print("\n")
    for i in range(len(spillere)):
        print(spillere[i])


if __name__ == '__main__':
    create_players()
    print("\n")
    create_questions()
    spill()