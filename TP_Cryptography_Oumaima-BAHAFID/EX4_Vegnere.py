import string
#__________________________ Chiffrement_____________________
def chiffrement_vigenere(texte_clair, cle):
    alphabet = string.ascii_uppercase
    texte_clair = texte_clair.upper().replace(" ", "")  # Met en majuscules et retire les espaces
    cle = cle.upper()
    
    texte_chiffre = ""
    cle_length = len(cle)
    cle_index = 0

    for lettre in texte_clair:
        if lettre in alphabet:
            # Obtenir l'index de la lettre et celui de la clé
            index_lettre = alphabet.index(lettre)
            index_cle = alphabet.index(cle[cle_index % cle_length])
            
            # Appliquer la formule de chiffrement : (Pi + Kj) mod 26
            index_chiffre = (index_lettre + index_cle) % len(alphabet)
            texte_chiffre += alphabet[index_chiffre]
            
            cle_index += 1
        else:
            texte_chiffre += lettre  # Garder les caractères non-alphabétiques inchangés
    
    return texte_chiffre

def ecrire_fichier_chiffre(output_file, texte_chiffre):
    with open(output_file, 'w') as f:
        f.write(texte_chiffre)

# Exemple d'utilisation
texte = "Voici un texte à chiffrer avec l'algorithme de Vigenère"
cle = "CLE"
texte_chiffre = chiffrement_vigenere(texte, cle)
ecrire_fichier_chiffre("texte_chiffre_vigenere.txt", texte_chiffre)
print("Texte chiffré :", texte_chiffre)


#____________________________ Déchifrement______________________
def dechiffrement_vigenere(texte_chiffre, cle):
    alphabet = string.ascii_uppercase
    texte_chiffre = texte_chiffre.upper().replace(" ", "")  # Met en majuscules et retire les espaces
    cle = cle.upper()
    
    texte_dechiffre = ""
    cle_length = len(cle)
    cle_index = 0

    for lettre in texte_chiffre:
        if lettre in alphabet:
            # Obtenir l'index de la lettre chiffrée et celui de la clé
            index_lettre = alphabet.index(lettre)
            index_cle = alphabet.index(cle[cle_index % cle_length])
            
            # Appliquer la formule de déchiffrement : (Ci - Kj) mod 26
            index_dechiffre = (index_lettre - index_cle) % len(alphabet)
            texte_dechiffre += alphabet[index_dechiffre]
            
            cle_index += 1
        else:
            texte_dechiffre += lettre  # Garder les caractères non-alphabétiques inchangés
    
    return texte_dechiffre

def lire_fichier_chiffre(input_file):
    with open(input_file, 'r') as f:
        return f.read()

# Exemple d'utilisation
texte_chiffre = lire_fichier_chiffre("texte_chiffre_vigenere.txt")
texte_dechiffre = dechiffrement_vigenere(texte_chiffre, cle)
print("Texte déchiffré :", texte_dechiffre)
