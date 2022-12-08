class Automobil:
    numar_roti = 4      # definim atribute
    forma = None
    culoare = None
    numar_usi = 2


    def printeaza_nr_roti(self):            # definim metode
        if self.numar_roti == 2:
            print(f'numarul de roti {self.numar_roti}')
            print('automobilul meu este motocicleta')

    def printeaza_forma(self, tablarie):
        self.forma = tablarie     # atributul metodei il folosim in suprascrierea metodei(forma din clasa are alta val)
        if self.forma == 'SUV':
            print(f' forma este {self.forma}')
            print(f'automobilul este SUV')

    def printeaza_culoare(self):
        self.culoare = 'mov'

    def printeaza_usi(self):
        if self.numar_usi == 2:
            print(f' usile sunt {self.numar_usi}')
            print(f'automobilul este sport')
        elif self.numar_usi == 4:
            print(f' usile sunt {self.numar_usi}')
            print(f'automobilul este masina de familie')
        elif self.numar_usi == 0:
            print(f' usile sunt {self.numar_usi}')
            print(f'automobilul este motocicleta')



caruta = Automobil()        # initializare. clasa automobil initializata in obiectul caruta
# acum folosim propietatile obiectului caruta

# apelarea de atribute
print(caruta.numar_usi)

# apelarea de metode
caruta.printeaza_usi()

#  apelarea de metode cu argumente
caruta.printeaza_forma('SUV')