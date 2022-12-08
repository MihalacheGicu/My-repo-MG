# a = 5
# print(a)
# a += 3+a
# a = a+3+a
# print(a)
# if a == 21:
#     print('Am ajuns aici')
# elif a == 29:
#     print('suntem in elif')
# else:
#     print('Am ajuns in else')

# masina = 'sqoda'
#
# if masina.__contains__('sq'):
#     print('exista')
#     # masina = masina.__add__('20')
#     masina += '123'
#     print(masina)
#     print(type(masina[5]))
#     if int(masina[5]) == 1:
#         print('exista numar')

# variabila = 40
# if variabila in range(30,50):
#     numar = str(variabila) + ' ani'
#     print(numar)
#     # if numar.__contains__(' '):
#     # if numar[2]==' ':
#     if numar.find(' '):
#         print('exista numar')

pret = 678
if pret >= 678:
    elev = 'Ionel a luat nota 6'
    # print(a[:len(a) - 2:-1])
    nota = elev[:17:-1]
    # nota = int(elev[len(elev) - 1:len(elev):1])
    print(nota)
    nota = float(nota)
    if nota >= 4.5:
        print('ai trecut')