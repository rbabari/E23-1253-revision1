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

    def afficher(self):
        print('Je suis ', self.prenom, 'et j ai', self.age)


# Création des objets

p1 = Personne('babari', 'raouf', 31)
p2 = Personne('bachir', 'Fikry', 25)
p3 = Personne('Nabil', 'Agsous', 'immortel')


# Les objets de la même classe se comportemt souvent de la même manière ...

p1.afficher()

#Etudiant