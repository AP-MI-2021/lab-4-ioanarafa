def afisareNumereNegative(list):
    numereNegative = []
    for x in list:
        if x < 0:
            numereNegative.append(int(x))
    return numereNegative


def afisareUltimaCifra(list, nr):
    numereGasite = []
    for x in list:
        if int(str(x)[-1]) == nr:
            numereGasite.append(x)
    numarMinim = numereGasite[0]
    for y in numereGasite:
        if y < numarMinim:
            numarMinim = y
    return numarMinim


def inlocuiesteCuCmmdc(list):
    numerePozitive = []
    for x in list:
        if x >= 0:
            numerePozitive.append(x)
    return numerePozitive


def cmmdc(x, y):
    z = 0
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def printMenu():
    print("1.Citire lista")
    print("2.Afișarea tuturor numerelor negative nenule din listă")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("6.Inchide program")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def main():
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(afisareNumereNegative(l))
        elif optiune == "3":
            nr = int(input("Dati numarul de test: "))
            print(afisareUltimaCifra(l, nr))
        elif optiune == "4":
            print("problema4")
        elif optiune == "5":
            inlocuiesteCuCmmdc(l)
        elif optiune == "6":
            break
        else:
            print("Optiune gresita! Reincercati!")
main()


