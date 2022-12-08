# # def verifica_prezenta():
# #     lista = ['ionel', 'gigel', 'popescu']
# #     for index in range(2):
# #         print(lista[index])
# #         assert lista[index] is 'Ionel'
# # verifica_prezenta()
# # -----------------------------------------------
# string_masini = input('scrie o lista de masini cu ,: ')  # Volvo,Dacia,Audi,Tractor,Testla
# print(string_masini)
# lista_masini = string_masini.split(',')
#
#
# def returneaza_litere(portocala, mar = 5):
#     print(mar)
#     for masina in portocala:
#         if masina == 'Tractor':
#             for indexlitera in range(len(masina)):
#                 if masina[indexlitera] == 'b':
#                     return (masina[indexlitera])
#                 elif masina[indexlitera] == 't':    # s-a oprit la a si la return ul de mai sus, nu mai printeaza t
#                     return (masina[indexlitera])
#
#
# print(returneaza_litere(lista_masini,8))
# list1 = [0, 1, 2, 3]
# list2 = [0, 1, 4, 5]
# list3 = list1 + list2
# print(list(set(list3)))

index = 0
while index <= 5:
    list1 = [0, 1, 2, 3, 4]
    print(list1[index])
    index = index + 1
