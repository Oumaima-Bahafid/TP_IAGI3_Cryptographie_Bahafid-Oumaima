
# 1. Trouver l'inverse de nombre dans 26Z
def inverse_modulaire(n, mod=26):
    n = n % mod
    for x in range(1, mod):
        if (n * x) % mod == 1:
            return x
    return 0  # Si l'inverse n'existe pas

# Exemple d'utilisation
print("Inverse modulaire de 3 dans Z/26Z :", inverse_modulaire(3))



# 2. Générer une matrice inversible dans Z/26ZZ/26Z
import numpy as np
from math import gcd
import random

def generer_matrice_inversible():
    while True:
        # Générer une matrice 2x2 avec des coefficients aléatoires dans Z/26Z
        matrice = np.random.randint(0, 26, (2, 2))
        det = int(np.round(np.linalg.det(matrice))) % 26  # Calculer le déterminant modulo 26
        
        if gcd(det, 26) == 1:  # Vérifier que le déterminant est copremier avec 26
            return matrice

# Exemple d'utilisation
matrice_Q = generer_matrice_inversible()
print("Matrice inversible générée :", matrice_Q)


# Crypter un Text Avec Hill
def texte_en_vecteurs(texte):
    texte = texte.upper().replace(" ", "")
    vecteurs = []
    if len(texte) % 2 != 0:
        texte += 'X'  # Ajouter une lettre fictive si la longueur du texte est impaire

    for i in range(0, len(texte), 2):
        vecteurs.append([ord(texte[i]) - 65, ord(texte[i+1]) - 65])
    return vecteurs

def crypter_hill(texte, matrice_Q):
    vecteurs = texte_en_vecteurs(texte)
    texte_chiffre = ""

    for vecteur in vecteurs:
        # Multiplication matricielle et réduction modulo 26
        resultat = np.dot(matrice_Q, vecteur) % 26
        texte_chiffre += chr(int(resultat[0]) + 65) + chr(int(resultat[1]) + 65)
    
    return texte_chiffre

# Exemple d'utilisation
texte = "HELLO"
texte_chiffre = crypter_hill(texte, matrice_Q)
print("Texte chiffré avec Hill :", texte_chiffre)


# Decrypter Un Text Avec Hill
def inverse_matrice_modulaire(matrice, mod=26):
    det = int(np.round(np.linalg.det(matrice))) % mod
    inv_det = inverse_modulaire(det, mod)
    
    if inv_det == 0:
        raise ValueError("La matrice n'est pas inversible modulo 26")
    
    adjugate = np.round(np.linalg.inv(matrice) * np.linalg.det(matrice)).astype(int)
    matrice_inverse = (inv_det * adjugate) % mod
    return matrice_inverse

def dechiffrer_hill(texte_chiffre, matrice_Q):
    matrice_inverse = inverse_matrice_modulaire(matrice_Q)
    vecteurs = texte_en_vecteurs(texte_chiffre)
    texte_dechiffre = ""

    for vecteur in vecteurs:
        # Multiplication matricielle avec la matrice inverse et réduction modulo 26
        resultat = np.dot(matrice_inverse, vecteur) % 26
        texte_dechiffre += chr(int(resultat[0]) + 65) + chr(int(resultat[1]) + 65)
    
    return texte_dechiffre

# Exemple d'utilisation
texte_dechiffre = dechiffrer_hill(texte_chiffre, matrice_Q)
print("Texte déchiffré avec Hill :", texte_dechiffre)


# Application
# 1. Calculer l'inverse modulaire
print("Inverse modulaire de 7 dans Z/26Z :", inverse_modulaire(7))

# 2. Générer une matrice inversible
matrice_Q = generer_matrice_inversible()
print("Matrice inversible générée :", matrice_Q)

# 3. Chiffrer un texte
texte = "HELLO"
texte_chiffre = crypter_hill(texte, matrice_Q)
print("Texte chiffré :", texte_chiffre)

# 4. Déchiffrer le texte
texte_dechiffre = dechiffrer_hill(texte_chiffre, matrice_Q)
print("Texte déchiffré :", texte_dechiffre)
