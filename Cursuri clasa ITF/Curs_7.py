# # tratarea exceptiilor
# try:
#     assert 1 == 2, 'comparatia nu este corecta' # prop dintre ghilimele este atribuita AssertionError
# except AssertionError as e:  # setare a unui alias ca e
#     print(e, 'programul nu a executat linia respectiva')
# print('hello')
# -----------------
from abc import abstractmethod, ABC


# # mostenire sau inheritance:
# class Masina:
#     def numar_roti(self):
#         print('masina are 4 roti')
#
#
# class Jeep(Masina):
#     def suspensii(self):
#         print('Jeep ul are suspensii mari')
#
#
# hummer = Jeep()
# hummer.numar_roti()
# hummer.suspensii()
# logan = Jeep()
# logan.numar_roti()
# logan.suspensii()
# ford = Masina()
# ford.numar_roti()
# -------------------

# polimorfism
class Masina(ABC):  # aici implementam o clasa abstracta(o interfata)
    @abstractmethod
    def numar_roti(self):
        raise NotImplementedError

    @abstractmethod
    def culoare(self):
        raise NotImplementedError


class SUV(Masina):
    def __suspensii(self):
        print('Jeep ul are suspensii mari')

    def numar_roti(self):  # abstractizare pana jos
        print('4 roti de teren')

    def culoare(self):
        print('neagra')


class Sport(Masina):
    def numar_roti(self):  # abstractizare pana jos
        print('4 roti de circuit')

    def culoare(self):
        print('albastra')


ferrari = Sport()
ferrari.numar_roti()
volvo = SUV()
volvo.culoare()  # implementare polimorfism
ferrari.culoare()  # implementare polimorfism

# incapsularea (cu '__' mai sus la metoda suspensii din SUV mai sus) cu tratarea erorilor
# volvo.suspensii()
try:
    volvo.suspensii()
except AttributeError:
    print('sunt expert la erori')
except NameError:
    print('test')
