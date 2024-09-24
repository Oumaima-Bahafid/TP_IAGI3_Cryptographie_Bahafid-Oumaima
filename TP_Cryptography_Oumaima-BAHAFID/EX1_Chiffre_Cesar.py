#______1_________________________________
def cesar_encrypt(ch, k):
    encrypted = ""
    for char in ch:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            shift = ord('A') if char.isupper() else ord('a')  # Identifie si c'est une majuscule ou minuscule
            # Applique le décalage, puis ramène dans l'intervalle des lettres
            encrypted += chr((ord(char) - shift + k) % 26 + shift)
        else:
            encrypted += char  # Garde les caractères non alphabétiques inchangés
    return encrypted

#_______________2______________
def cesar_encrypt(ch, k):
    encrypted = ""
    for char in ch:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            shift = ord('A') if char.isupper() else ord('a')  # Identifie si c'est une majuscule ou minuscule
            # Applique le décalage, puis ramène dans l'intervalle des lettres
            encrypted += chr((ord(char) - shift + k) % 26 + shift)
        else:
            encrypted += char  # Garde les caractères non alphabétiques inchangés
    return encrypted

# 3_________________ Programme de chifferement et déchiffrement
def cesar_decrypt(ch, k):
    # Pour déchiffrer, il suffit de faire un décalage inverse
    return cesar_encrypt(ch, -k)

# Programme principal pour lire une chaîne de caractères, appliquer le cryptage et le décryptage
if __name__ == "__main__":
    ch = input("Entrez la chaîne à chiffrer : ")
    k = int(input("Entrez le décalage (1-25) : "))

    encrypted = cesar_encrypt(ch, k)
    print(f"Chaîne cryptée : {encrypted}")

    decrypted = cesar_decrypt(encrypted, k)
    print(f"Chaîne décryptée : {decrypted}")


#4_____________________ CryptAnlayse en utilsant Brute Force
def cesar_cryptanalysis(ch):
    print("Cryptanalyse :")
    for k in range(1, 26):
        decrypted = cesar_decrypt(ch, k)
        print(f"Décalage {k}: {decrypted}")

# Programme principal pour la cryptanalyse
if __name__ == "__main__":
    intercepted_message = input("Entrez le message intercepté : ")
    cesar_cryptanalysis(intercepted_message)
