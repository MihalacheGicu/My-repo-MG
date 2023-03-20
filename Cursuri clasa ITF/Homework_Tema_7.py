from abc import ABC

# """
# Tema 7 - OOP _ Cei 4 Piloni
# 1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
# acum la ore.
# Curs git/github https://bit.ly/3yfFvqL
# VIDEOS 1, 2 si 3
#
#
# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).
#
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
#
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
#
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
# """


class FormaGeometrica(ABC):
    PI = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura ** 2

    def descrie(self):
        print("Sunt patrat si am colturi")

    def get_latura(self):
        print(f"Apelam latura {self.__latura}")
        return self.__latura

    def set_latura(self, latura_noua):
        print("Schimbam valoarea laturei")
        self.__latura = latura_noua

    def del_latura(self):
        print("Stergem valoarea laturei cu del sau schimbam valoarea pe NONE. "
              "In acest caz doar modificam valoarea in 0")
        self.__latura = 0

    latura_value = property(get_latura, set_latura, del_latura)


patrat_mic = Patrat(4)
patrat_mic.latura_value = 2
print(patrat_mic.latura_value)
print(patrat_mic.aria())
del patrat_mic.latura_value


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza * self.PI

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, noua_raza):
        if noua_raza < 0:
            print("Nu se poate seta o valaoare mai mica de 0")
        else:
            self.__raza = noua_raza

    @raza.deleter
    def raza(self):
        self.__raza = 0


cerc_mediu = Cerc(6)
print(cerc_mediu.raza)
cerc_mediu.raza = 4
print(cerc_mediu.raza)
print(cerc_mediu.aria())
del cerc_mediu.raza
print(cerc_mediu.raza)
cerc_mediu.descrie()

lista_forme_geometrice = [
    Cerc(8),
    Cerc(4),
    Patrat(8),
    Patrat(4)
]

for forma in lista_forme_geometrice:
    print(f"Aria {forma.aria()}")
