"""
Une petie révision ::
"""

# Qu'est ce que une classe / Objet ?
# Une classe contient des attributs (data) et des méthodes (comportement / traitement)
# Une classe Est un concept abstrait qui permet de créer des objets concrets
# La classe se trouve dans le fichiers et les objets se trouvent dans la mémoire

# Le constructeur permet de créer des objets

# 4 pliers de l'OO : encapsulation / abstraction / héritage / polymorphisme

#class ::
class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age

    def presenteToi(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)

#class Etudiant hérite de Personne ::
class Etudiant(Personne):
    # constructeur en utilisant un objet de type Personne (parent)
    def __init__(self, p_personne, p_NumEtudiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_personne.nom, p_personne.prenom, p_personne.age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneeGraduation =p_AnneeGraduation

    def presenteToi(self):
        print('Je suis ', self.prenom, 'et suis dans le gr : ', self.Groupe)

"""
  # constructeur V2 en utilisant un objet de type Personne (parent)
    def __init__(self, p_nom, p_prenom, p_age, p_NumEtudiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_nom, p_prenom, p_age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneeGraduation =p_AnneeGraduation
"""

# Un Etudiant(+NumEtudiant, Groupe, AnneeGraduation) est une Personne(nom,prenom,age)
# Un Employé(+NumEmployee, Service, Bureau) == c'est une Personne
# Un Enseignant ( + Département) est un Employé


# Création des objets : Instantiation

liste = []
liste.append(Personne('babari', 'raouf', 31))
liste.append(Personne('bachir', 'Fikry', 25))
liste.append(Personne('Nabil', 'Agsous', 40))

E1 = Etudiant(liste[1], 1234567, 1253, 2024)
E2 = Etudiant(Personne('Nabil', 'Agsous', 40), 1234567, 1253, 2024)
liste.append(E1)
liste.append(E2)

# constructeur V2 : E3 = Etudiant('Nabil', 'Agsous', 40, 1234567, 1253, 2024)

# Les objets de la même classe se comportemt souvent de la même manière ...



for x in liste:
    x.presenteToi()


#Exercice Créer une liste de 4 Voiture
# Trouver un moyen pour informer quelle personne conduit quelle voiture ???
