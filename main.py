import translator as tr

t = tr.Translator()
#def AssegnaTraduzione():
    #with open file("dictionary.txt", "r") as f:

t.loadDictionary("dictionary.txt")
while(True):

    t.printMenu()

    txtIn = input("Scegli numero")

    # Add input control here!

    if int(txtIn) == 1:
        num = input("Ok, quale parola devo aggiungere?")
        t.handleAdd(num)
        #print(f"{tupla} \n Aggiunta!")
    if int(txtIn) == 2:
        num = input("Ok, quale parola devo tradurre?")
        t.handleTranslate(num)
        #print(f"La traduzione di {txtIn} è {parolaTradotta}")
    if int(txtIn) == 3:
        num = input("Ok, quale parola devo cercare?").lower()
        t.handleWildCard(num)
        # print(f"{parolaTrovata.split(" ")[1]} \n {parolaTrovata.split(" ")[0]}")
    if int(txtIn) == 4:
        t.dictionary.printAll()
    if int(txtIn) == 5:
        break
    else:
        print("Scelta non valida")
