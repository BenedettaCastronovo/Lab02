import re
import fnmatch

class Dictionary:
    def __init__(self):
        self.words = {} #dizionario

    def addWord(self, alien_word, translation):
        # controllo caratteri ammessi
        #if not re.fullmatch(r"[a-zA-Z]+", alien_word) or not re.fullmatch(r"[a-zA-Z]+", translation):
        if not alien_word.isalpha():
            raise ValueError("Sono ammessi solo caratteri alfabetici!")

        for t in translation:
            if not t.isalpha():
                raise ValueError("Sono ammessi solo caratteri alfabetici!")

        alien_word = alien_word.lower()
        translation = translation.lower()

        if alien_word in self.words:
            print(f"Parola {alien_word} già esistente!")
            return

        self.words[alien_word] = translation

        for t in translation:
            t = t.lower()
            if t not in self.words[alien_word]:
                self.words[alien_word].append(t)

    def translate(self, alien_word):
        alien_word = alien_word.lower()
        return self.words.get(alien_word, None)
    def translateWordWildCard(self, pattern):
        pattern = pattern.lower()
        ris = []

        for word in self.words:
            if fnmatch.fnmatch(word, pattern):
                ris.append(word)

        return ris

    def printall(self):
        for k, v in self.words.items():
            print(f"{k} -> {', '.join(v)}")