# Tuto funkci implementuj. Smaz prikaz 'pass' a pis telo funkce.
def word_frequency(text):
    slovnik = {}
    slovo = ""
    text = text.lower()
    for i in text:
        i = i
        if i.isalpha() == True:
            slovo = slovo + i
        else:
            if slovo.isalpha() == True:
                if slovo in slovnik:
                    slovnik[slovo] = slovnik[slovo] + 1
                else:
                    slovnik[slovo] = 1
                slovo = ""
    if i == text[len(text)-1] and i.isalpha() == True:
        if slovo in slovnik:
            slovnik[slovo] = slovnik[slovo] + 1
        else:
            slovnik[slovo] = 1
    return slovnik

# testy (upravujte dle libosti)
print(word_frequency("Ksi, Ksa, Ksi, Kse"))       # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Ksi,+Ksa,Ksi;;-;Kse_"))     # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Informatika je nejlepsi"))  # {'informatika': 1, 'je': 1, 'nejlepsi': 1}

