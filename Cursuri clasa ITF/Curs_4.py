# propozitie = 'Ana are meRe'
# for litera in propozitie:
#     # if litera == 'r' or litera == 'R':
#     if litera.upper() == 'R':   # le-a marit pe ambele si le-a afisat asa cum sunt nemodificate(metoda)
#         print(litera)

# index = 1
# while 23 >= index:  # ctrl alt l - aliniere cod
#     index += 1
#     print(index)
#     if index <= 25:
#         print('maine este vineri')
#         if index == 25:
#             break  # lipseste incrementarea: += si nu ruleaza decat la conditie ==
# print(index)
# else:
# print('am terminat de printat')

# propozitie2 = 'Ana are mere'
# for index in range(10):
#     if index == 5:
#         continue
#     print(propozitie2[index])
# else:
#     print('am terminat')

paine = ['paine alba', 'paine Graham', 'paine secara']
lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
for cumparatura in lista_cumparaturi:
    print(type(cumparatura))
    if type(cumparatura) == list:
        # print(cumparatura)
        cumparatura_clona = cumparatura
        lista_cumparaturi.remove(cumparatura)
        lista_cumparaturi.extend(cumparatura_clona)
print(lista_cumparaturi)
        # for subprodus in produs:
        #     print(subprodus)

# Andreea
# paine = ['paine alba', 'paine Graham', 'paine secara']
# lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
# lista_cumparaturi2 = []
# for produs in lista_cumparaturi:
#     if type(produs) == list:
#         for subprodus in produs:
#             print(subprodus)
#             lista_cumparaturi2.append(subprodus)
#     else:
#         #print(produs)
#         lista_cumparaturi2.append(produs)
# print(lista_cumparaturi2)
#