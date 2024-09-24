import random
from collections import defaultdict

# Fonction pour générer un tableau de substitution homophone
def generer_tableau_substitution_homophone():
    # On génère les nombres de 0 à 99 et on les mélange
    numbers = list(range(100))
    random.shuffle(numbers)
    
    # On définit un tableau de substitution pour les lettres de A à Z (26 lettres)
    # Par exemple, 4 substitutions pour chaque lettre
    tab_substitution = defaultdict(list)
    
    # Attribuer 4 nombres aléatoires pour chaque lettre
    for i, lettre in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        tab_substitution[lettre] = numbers[i*4:(i+1)*4]  # 4 valeurs par lettre
    
    return tab_substitution

# Fonction pour crypter un texte par chiffre homophone
def crypter_texte_homophone(texte, tab_substitution):
    # Dictionnaire pour garder la trace des substitutions restantes par lettre
    utilisation_restante = defaultdict(list)
    
    # Initialiser les substitutions restantes pour chaque lettre
    for lettre in tab_substitution:
        utilisation_restante[lettre] = tab_substitution[lettre][:]
        random.shuffle(utilisation_restante[lettre])
    
    # Liste pour stocker le texte crypté
    texte_crypte = []
    
    # Pour chaque lettre dans le texte à crypter
    for char in texte.upper():
        if char in tab_substitution:  # Si c'est une lettre de l'alphabet
            # Vérifier si toutes les valeurs ont été utilisées, réinitialiser si nécessaire
            if not utilisation_restante[char]:
                utilisation_restante[char] = tab_substitution[char][:]
                random.shuffle(utilisation_restante[char])
            
            # Choisir un substitut aléatoire pour cette lettre
            chiffre = utilisation_restante[char].pop(0)
            # Ajouter le chiffre crypté au texte final
            texte_crypte.append(f"{chiffre:02}")  # Format à 2 chiffres
        else:
            # Si ce n'est pas une lettre, ajouter le caractère tel quel (espaces, ponctuation, etc.)
            texte_crypte.append(char)
    
    # Retourner le texte crypté sous forme de chaîne
    return " ".join(texte_crypte)

# Exemple d'utilisation
tab_substitution = generer_tableau_substitution_homophone()
print("Tableau de substitution homophone :")
for lettre, valeurs in tab_substitution.items():
    print(f"{lettre}: {valeurs}")

# Exemple de texte à crypter
texte = "HELLO WORLD"
texte_crypte = crypter_texte_homophone(texte, tab_substitution)

print(f"Texte original : {texte}")
print(f"Texte crypté : {texte_crypte}")



#___________________________________________________________________________________
#Code Avec crypto de Pylob
print(f"Pylob")
def generer_carre_polybe():
    # On initialise le carré de Polybe avec un alphabet sans la lettre J (fusion avec I)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    carre_polybe = {}
    
    # On remplit la grille 5x5 avec les lettres
    ligne = 1
    for i in range(0, len(alphabet), 5):
        for colonne in range(1, 6):
            lettre = alphabet[i + (colonne - 1)]
            carre_polybe[lettre] = (ligne, colonne)
        ligne += 1
    
    return carre_polybe

def crypter_polybe(texte, carre_polybe):
    texte_crypte = []
    
    for char in texte.upper():
        if char in carre_polybe:
            ligne, colonne = carre_polybe[char]
            texte_crypte.append(f"{ligne}{colonne}")
        else:
            # Garder les caractères non alphabétiques
            texte_crypte.append(char)
    
    return " ".join(texte_crypte)

# Exemple d'utilisation
carre_polybe = generer_carre_polybe()
print("Carré de Polybe :")
for lettre, coordonnees in carre_polybe.items():
    print(f"{lettre}: {coordonnees}")

texte = "HELLO WORLD"
texte_crypte = crypter_polybe(texte, carre_polybe)
print(f"Texte original : {texte}")
print(f"Texte crypté : {texte_crypte}")




#_________ Alternative 2
print("Alternative 2")

# Tableau basé sur l'alternative 2 de l'image
tableau_alternative_2 = {
    "E": [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
          (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
    "A": [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)],
    "S": [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)],
    "T": [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8)],
    "R": [(1, 9), (2, 9), (3, 9), (4, 9), (5, 9)],
    "I": [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5)],
    "B": [(6, 6)],
    "C": [(6, 7)],
    "D": [(6, 8)],
    "F": [(6, 9)],
    "L": [(7, 1), (7, 2), (7, 3)],
    "G": [(7, 4)],
    "H": [(7, 5)],
    "K": [(7, 6)],
    "M": [(7, 7)],
    "N": [(8, 1), (8, 2), (8, 3)],
    "O": [(8, 4)],
    "P": [(8, 5)],
    "Q": [(8, 6)],
    "V": [(8, 7)],
    "U": [(9, 1)],
    "W": [(9, 2)],
    "X": [(9, 3)],
    "Y": [(9, 4)],
    "Z": [(9, 5)]
}

def crypter_alternative_2(texte, tableau):
    texte_crypte = []
    
    for char in texte.upper():
        if char in tableau:
            # Choisir une paire ligne/colonne aléatoire pour la lettre
            ligne, colonne = random.choice(tableau[char])
            texte_crypte.append(f"{ligne}{colonne}")
        else:
            texte_crypte.append(char)  # Garder les caractères non alphabétiques
    
    return " ".join(texte_crypte)

# Exemple d'utilisation
texte = "HELLO WORLD"
texte_crypte = crypter_alternative_2(texte, tableau_alternative_2)
print(f"Texte original : {texte}")
print(f"Texte crypté : {texte_crypte}")
