from idlelib.pyparse import trans

import dictionary as d
import fnmatch

diz = d.Dictionary()  #importo la classe


class Translator:

    def __init__(self):
        self.dictionary = diz

    def printMenu(self):
        print(f"1. Aggiungi nuova parola")
        print(f"2. Cerca una traduzione")
        print(f"3. Cerca con wildcard")
        print(f"4. Stampa tutto il dizionario")
        print(f"5. Exit")

    def loadDictionary(self, dict):
        #dizionario = []
        file = open(dict, "r", encoding="utf-8")  # dict is a string with the filename of the dictionary
        for line in file:
            campi = line.strip()
            if len(campi.split(" ")) > 2:
                raise IndexError
            alien, translation = campi.split()
            self.dictionary.addWord(alien, translation)
        file.close()
        #return self.dictionary

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        try:
            parts = entry.split(" ")
            if len(parts) < 2:
                raise ValueError
            alien = parts[0]
            translations = parts[1:]
            self.dictionary.addWord(alien, translations)
            with open("dictionary.txt", "w") as f:
                for k, v in self.dictionary.words.items():
                    f.write(f"{k} {' '.join(v)}\n")
        #return entry  ###
        except ValueError:
            print("Formato errato. Usa: parola traduzione")

        except Exception as e:
            print(e)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        result = self.dictionary.translate(query)
        if result:
            print(f"La traduzione è: {', '.join(result)}")
        else:
            print("Parola non trovata")

    def handleWildCard(self, query):
        results = self.dictionary.translateWordWildCard(query)
        if results:
            for word in results:
                trad = self.dictionary.words[word]
                print(f"{word} -> {', '.join(trad)}")
        else:
            print("Nessuna parola trovata")
