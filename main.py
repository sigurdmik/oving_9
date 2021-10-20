import os
import sys



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
        riktig_svar = int(self.riktig_svar)
        if avgitt_svar == (riktig_svar+1):                                          #Bruker riktig_svar +1 fordi jeg vil at brukeren skal svare med spm nummeret ikke index
            return 1
        else:
            return 0



                                                                                    #Listen som vil inneholde alle spørsmålene etter create_questions() har kjørt
questions = []

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
    poeng = 0
    full_score = len(questions)
    for i in range(full_score):
        print(questions[i])
        if questions[i].sjekk_svar() == 1:
            poeng += 1
        print("\n")
    print(f"Du fikk {poeng}/{full_score} riktige")


if __name__ == '__main__':
    create_questions()
    spill()