import string
import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def nom_pres(titre):
    L = []
    titre = titre[:len(titre)-4]
    titre = titre[11:]
    if ord(titre[len(titre)-1]) <= 57:
        titre = titre[:-1]
    return titre

def prenom_pres(nom):
    prenom = ""
    if nom == "Chirac":
        prenom = "Jacques"
    if nom == "Giscard d'Estaing":
        prenom = "Valérie"
    if nom == "Hollande":
        prenom = "François"
    if nom == "Macron":
        prenom = "Emmanuel"
    if nom == "Mitterand":
        prenom = "François"
    if nom == "Sarkozy":
        prenom = "Nicolas"
    return prenom

# mettre en minuscule les textes

def convertir_en_minuscules(input_dir, output_dir, file_names, file_names_cleaned):
    # Assurez-vous que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parcourez chaque fichier d'entrée et de sortie
    for input_name, output_name in zip(file_names, file_names_cleaned):
        input_path = os.path.join(input_dir, input_name)
        output_path = os.path.join(output_dir, output_name)

        # Vérifiez si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as input_file:
                # Lire le contenu du fichier et le convertir en minuscules
                content = input_file.read().lower()

                # Écrire le contenu dans le fichier de sortie b
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(content)



# enlever ponctuation

def nettoyer_texte(texte):
    # Supprimer la ponctuation
    ponctuation = string.punctuation
    texte_nettoye = ''.join(caractere if caractere not in ponctuation else ' ' for caractere in texte)
    return texte_nettoye

#appliquer la fonction nettoyer_texte sur un fichier
def traiter_fichier(nom_fichier):
    chemin_fichier = os.path.join('cleaned', nom_fichier)

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()
        texte_nettoye = nettoyer_texte(texte)

    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte_nettoye)


#appliquer la fonction traiter_fichier sur un repertoire
def parcourir_repertoire():
    repertoire = 'cleaned'
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier.endswith('.txt'):
            traiter_fichier(nom_fichier)





## Début Matrice TF-IDF ##

    # TF
def dictionnaire(input_dir, file_names_cleaned):
    # Initialiser le dictionnaire des occurrences en dehors de la boucle
    occurrence = {}

    # Parcourir chaque fichier
    for input_name in file_names_cleaned:
        input_path = os.path.join(input_dir, input_name)

        # Vérifiez si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as fichier:
                content = fichier.read()

                # Diviser le contenu en mots
                mots = content.split()

                # Parcourir chaque mot et mettre à jour le dictionnaire des occurrences
                for mot in mots:
                    # Mettre à jour le dictionnaire des occurrences
                    occurrence[mot] = occurrence.get(mot, 0) + 1

    # Trier le dictionnaire des occurrences par nombre d'occurrences décroissant
    occurrence_triees = dict(sorted(occurrence.items(), key=lambda x: x[1], reverse=True))

    # Retourner le dictionnaire trié
    return occurrence_triees


#IDF

def calculer_idf(repertoire_corpus):
    # Initialiser le dictionnaire pour stocker le nombre de documents contenant chaque mot
    documents_contenant_mot = {}

    # Nombre total de documents dans le corpus
    total_documents = 0

    # Parcourir chaque fichier dans le répertoire du corpus
    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            total_documents += 1

            # Lire le contenu du fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                # Diviser le contenu en mots
                mots = contenu.split()

                # Identifier les mots uniques dans le fichier
                mots_uniques = set(mots)

                # Mettre à jour le dictionnaire des documents contenant chaque mot
                for mot in mots_uniques:
                    documents_contenant_mot[mot] = documents_contenant_mot.get(mot, 0) + 1

    # Calculer le score IDF pour chaque mot
    idf_scores = {}
    for mot, nb_documents_contenant in documents_contenant_mot.items():
        idf_scores[mot] = math.log(total_documents / (1 + nb_documents_contenant))

    return idf_scores


#TF-IDF











