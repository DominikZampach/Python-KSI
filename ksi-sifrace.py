def encode(n: int, plain_text: str) -> str: # vraci ciphertext typu String
    castSlova = ""
    rozdeleneSlovo = []
    for i in range(len(plain_text)):  #rozdeleni na casti po n-ticich
        castSlova = castSlova + str(plain_text[i])
        if (i+1)%n==0:
            rozdeleneSlovo.append(castSlova)
            castSlova = ""
    if castSlova != "":
        rozdeleneSlovo.append(castSlova)
    
    cipher_text = ""
    for j in range(len(rozdeleneSlovo)):
        rozdeleneSlovo[j] = rozdeleneSlovo[j][::-1] #reverse stringu
        cipher_text = cipher_text + str(rozdeleneSlovo[j])
    return cipher_text

def decode(n: int, cipher_text: str) -> str: # vraci plaintext typu String 
    #Dalo se i zavolat metodu encode, ale co už :DD
    castSlova = ""
    rozdeleneSlovo = []
    for k in range(len(cipher_text)):
        castSlova = castSlova + cipher_text[k]
        if (k+1)%n==0:
            rozdeleneSlovo.append(castSlova)
            castSlova = ""
    if castSlova != "":
        rozdeleneSlovo.append(castSlova)
        
    plain_text = ""
    for l in range(len(rozdeleneSlovo)):
        rozdeleneSlovo[l] = rozdeleneSlovo[l][::-1]
        plain_text = plain_text + str(rozdeleneSlovo[l])
    return plain_text

# Testy:
print(encode(3, "Ahoj")) # ohAj
print(encode(2, "Ahoj")) # hAjo
print(encode(10, "Ahoj")) # johA
print(encode(3, "12345")) # 32154
print(encode(5, "komunikace")) # numokecaki
print(decode(2, "hAjo")) # Ahoj
print(decode(5, "rgorpavomain")) # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane

# na automaticke testy doporucuji assert

