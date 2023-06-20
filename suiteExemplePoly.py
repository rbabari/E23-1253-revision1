"""
Une petie révision ::
"""
# https://www.w3schools.com/python/python_polymorphism.asp
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
        print('Personne [Je suis ', self.prenom, 'et j ai', self.age, ']')

#class Etudiant hérite de Personne ::
class Etudiant(Personne):
    # constructeur en utilisant un objet de type Personne (parent)
    def __init__(self, p_personne, p_NumEtudiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_personne.nom, p_personne.prenom, p_personne.age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneeGraduation =p_AnneeGraduation

    def presenteToi(self):
        print('Etudiant [ Je suis ', self.prenom, 'et suis dans le gr : ', self.Groupe, ']')

#class Etudiant hérite de Personne ::
class Emplyee(Personne):
    # constructeur en utilisant un objet de type Personne (parent)
    def __init__(self, p_personne, p_numEmployee, p_service, p_bureau):
        super().__init__(p_personne.nom, p_personne.prenom, p_personne.age)
        self.numEmployee = p_numEmployee
        self.service = p_service
        self.bureau =p_bureau

    def presenteToi(self):
        print('Emplyee [ Je suis ', self.prenom, 'et suis dans le service : ', self.service, ']')


class Enseignant(Emplyee):
    def __init__(self, p_employee, p_departement):
        super().__init__(Personne(p_employee.nom, p_employee.prenom, p_employee.age), p_employee.numEmployee, p_employee.service, p_employee.bureau)
        self.departement = p_departement

    def presenteToi(self):
        print('Enseignant [ Je suis ', self.prenom, 'et suis dans le departemnt : ', self.departement, ']')


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
Emp1 = Emplyee(Personne('babari', 'raouf', 26),  1234, 'Informatique', 'H12')
Ens1 = Enseignant(Emp1, 'dep Informatique')


liste.append(E1)
liste.append(E2)
liste.append(Emp1)
liste.append(Ens1)
# constructeur V2 : E3 = Etudiant('Nabil', 'Agsous', 40, 1234567, 1253, 2024)

# Les objets de la même classe se comportemt souvent de la même manière ...



for x in liste:
    x.presenteToi()


#Exercice Créer une liste de 4 Voiture
# Trouver un moyen pour informer quelle personne conduit quelle voiture ???
