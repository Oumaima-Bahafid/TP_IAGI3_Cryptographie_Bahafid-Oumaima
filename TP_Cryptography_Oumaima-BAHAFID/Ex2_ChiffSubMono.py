#_________________1_____________________
import random
import string

def generer_table_substitution():
    alphabet = list(string.ascii_uppercase)
    substitution = alphabet[:]  # Faire une copie de l'alphabet
    random.shuffle(substitution)  # Mélanger les lettres pour obtenir une substitution aléatoire
    table_substitution = dict(zip(alphabet, substitution))  # Créer un dictionnaire de substitution
    return table_substitution

# Exemple d'utilisation
table = generer_table_substitution()
print("Table de substitution générée :", table)

#________________2___________________
# Chiffrer un fichier texte par substitution mono-alphabétique

def chiffrer_texte_fichier(input_file, output_file, table_substitution):
    with open(input_file, 'r') as f:
        texte_clair = f.read().upper()
    
    texte_chiffre = ''
    for char in texte_clair:
        if char in table_substitution:
            texte_chiffre += table_substitution[char]
        else:
            texte_chiffre += char  # Garder les caractères non-alphabétiques inchangés
    
    with open(output_file, 'w') as f:
        f.write(texte_chiffre)

# Exemple d'utilisation

chiffrer_texte_fichier('Crypto.txt','outputFileSM.txt',table)
#________________________________________________________________________________________________________________________________

# 3 Calculer la fréquence d'apparition des lettres dans un texte
from collections import Counter

def calculer_frequence_lettres(texte):
    # Ignorer les espaces et autres caractères non-alphabétiques
    texte_filtre = [char for char in texte if char.isalpha()]
    total_lettres = len(texte_filtre)
    
    compteur_lettres = Counter(texte_filtre)
    frequences = {lettre: (compte / total_lettres) * 100 for lettre, compte in compteur_lettres.items()}
    
    # Trier les fréquences par ordre décroissant
    frequences_triees = dict(sorted(frequences.items(), key=lambda item: item[1], reverse=True))
    return frequences_triees
print("________________________________________________________________")
# Exemple d'utilisation
texte = "Genie Informatique et intelligence artificielle."
frequences = calculer_frequence_lettres(texte.upper())
print("Fréquences des lettres :", frequences)

print("________________________________________________________________")
# Cryptanalyser en se basan sur les frequences 
# Table de fréquences en français (vous pouvez utiliser une table pour l'anglais)
frequence_francaise = {
    'E': 14.69, 'A': 8.01, 'I': 7.54, 'S': 7.18, 'N': 6.89, 'R': 6.49, 
    'T': 6.12, 'L': 5.63, 'U': 5.29, 'O': 4.83, 'D': 3.66
}

def cryptanalyse_frequence(texte_chiffre, frequence_langue):
    # Étape 1: Calculer les fréquences du texte chiffré
    frequences_texte = calculer_frequence_lettres(texte_chiffre)
    
    # Étape 2: Associer les fréquences les plus élevées
    substitution_proposee = {}
    
    # Trier les lettres par fréquence décroissante
    lettres_chiffrees_triees = list(frequences_texte.keys())
    lettres_langue_triees = list(frequence_langue.keys())
    
    for i in range(min(len(lettres_chiffrees_triees), len(lettres_langue_triees))):
        substitution_proposee[lettres_chiffrees_triees[i]] = lettres_langue_triees[i]
    
    return substitution_proposee

# Exemple d'utilisation
texte_chiffre = "SR UWI IYG CISSI "
substitution = cryptanalyse_frequence(texte_chiffre, frequence_francaise)
print("Substitution proposée :", substitution)
