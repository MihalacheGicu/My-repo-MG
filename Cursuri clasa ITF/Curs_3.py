# lista = [3, 5, [7, 8, 9]]
# print(lista)
# print(lista[2])
# print(lista[2][1])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict.keys())
# print(thisdict.get('brand'))

# json_dict = {
#     "1": {
#         "title": "example glossary",
# 		"2": {
#             "title": "S",
# 			"3": {
#                 "4": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }
#
# print(json_dict.get('1').get('2').get('3').get('4').get('SortAs'))
# print(json_dict.pop('SortAs'))
#
# a = {1, 56, 43, 43}
# print(a)
# print(a)
# print(a[2]) # nu se poate apela index.este set
#
#tuple

# a = (1, 56, 43, 43, 324, 235, 346)
# print(a)
# print(a[2])
# print(a[3])
#
# x = (45, 45)
# b = ()
# c = b.__add__(x)
# print(c)
# print(a.__add__(x))
# print(a + x)
# a = a + x # nu se pot adauga variabile noi(append)
# print(a)

# lista1 = [1, 2, 3, 4]
# lista1.reverse()
# print(lista1)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "old_year": 1964,
#     "year": {
#         "year": 2020
#     }
# }
# ctrl + alt + l rearanjare cod
# dict = set({})  #transf dictitonar in set
# print(dict)

key_elev = 'ionica'
value_elev = 2
dict1 = {}
# dict1["ionica"] = 2 #introdus key si valoare in dict1 gol
dict1[key_elev] = value_elev
print(dict1)
