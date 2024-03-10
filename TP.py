# Ioan Domingues SN1
class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class Chaussette:
    def __init__(self, couleur, taille):
        self.couleur = couleur
        self.taille = taille

class NoeudPile:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class MyStack:
    def __init__(self):
        self.taille_max = 4
        self.taille_actuelle = 0
        self.sommet = None

    def empiler(self, chaussette):
        if self.est_pleine():
            raise MyOutOfSizeException("La pile est pleine")
        nouveau_noeud = NoeudPile(chaussette, self.sommet)
        self.sommet = nouveau_noeud
        self.taille_actuelle += 1

    def depiler(self):
        if self.est_vide():
            raise MyEmptyStackException("La pile est vide")
        chaussette = self.sommet.valeur
        self.sommet = self.sommet.suivant
        self.taille_actuelle -= 1
        return chaussette

    def est_vide(self):
        return self.taille_actuelle == 0

    def est_pleine(self):
        return self.taille_actuelle == self.taille_max

if __name__ == '__main__':
    maPile = MyStack()
    chaussette1 = Chaussette("bleu", "M")
    chaussette2 = Chaussette("rouge", "L")
    chaussette3 = Chaussette("verte", "S")
    chaussette4 = Chaussette("jaune", "XL")

    maPile.empiler(chaussette1)
    maPile.empiler(chaussette2)
    maPile.empiler(chaussette3)
    maPile.empiler(chaussette4)

    try:
        maPile.empiler(Chaussette("noire", "XXL"))  # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)

    print(maPile.depiler().couleur)  # jaune
    print(maPile.est_vide())  # False
    print(maPile.depiler().couleur)  # verte
    print(maPile.est_vide())  # False
    print(maPile.depiler().couleur)  # rouge
    print(maPile.est_vide())  # False
    print(maPile.depiler().couleur)  # bleu
    print(maPile.est_vide())  # True

    try:
        print(maPile.depiler())
    except MyEmptyStackException as e:
        print(e)

