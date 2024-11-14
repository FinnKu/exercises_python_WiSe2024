def buchstaben_ändern(string, buchstabe):
    string_lower = string.lower()
    
    for v in "aeiou": #v Vokal
        new_sentence = [] #neue Liste mit geändertem Satz
        
        for char in string_lower:
            if char == buchstabe: #buchstabe ist das was der User eingibt
                new_sentence.append(v) #fügt einen Vokal hinzu
            else:
                new_sentence.append(char) #ursprünglicher Character bleibt bestehen
        
        print("".join(new_sentence))
        
buchstaben_ändern("banana", "a")

#buchstaben_ändern("Wie geht es Ihnen?", "e")