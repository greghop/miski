HASLO_BARDZO_MOCNE = "Podane hasło jest bardzo mocne ponieważ jest długie, zawiera duże, małe litery, cyfry oraz znaki specjalne"
HASLO_MOCNE = "Podane hasło jest mocne ponieważ jest dość długie, zawiera duże litery lub małe litery lub cyfry"
HASLO_SLABE = "Podane hasło jest słabe ponieważ jest za krótkie"
HASLO_POPULARNE = "Wygląda na to że twoje hasło to popularna sekwencja, hasło jest mało unikatowe, zmień je!"

haslo = input("Podaj hasło, które chcesz sprawdzić: ")
wielkieLitery = 0
maleLitery = 0
cyfry = 0
znakiSpecjalne = 0
listaZnakowUnikalnych = []

for znak in haslo:
    if znak.isupper():
        wielkieLitery += 1
    elif znak.islower():
        maleLitery += 1
    elif znak.isdigit():
        cyfry += 1
    else:
        znakiSpecjalne += 1

    if znak not in listaZnakowUnikalnych:
        listaZnakowUnikalnych.append(znak)

print("###############Analiza hasła###############")
print(
    f"Długość hasła: {str(len(haslo))} \n \
Liczba wielkich liter: {str(wielkieLitery)} \n \
Liczba małych liter: {str(maleLitery)} \n \
Liczba cyfr: {str(cyfry)} \n \
Liczba znaków specjalnych: {str(znakiSpecjalne)} \n \
Unikatowe znaki: {listaZnakowUnikalnych} \n \
Liczba unikatowych znaków: {str(len(listaZnakowUnikalnych))}"
)


procentUnikatow = len(listaZnakowUnikalnych) * 100 / len(haslo)

if (
    len(haslo) >= 14
    and procentUnikatow >= 40
    and wielkieLitery != 0
    and maleLitery != 0
    and cyfry != 0
    and znakiSpecjalne != 0
):
    print(HASLO_BARDZO_MOCNE)
elif (
    len(haslo) < 14 and len(haslo) >= 8
    and procentUnikatow >= 40
    and wielkieLitery != 0
    and maleLitery != 0
    and cyfry != 0
):
    print(HASLO_MOCNE)
elif len(haslo) < 8:
    print(HASLO_SLABE)
else:
    print(HASLO_POPULARNE)
