class Figura_geometrica:
    lungime_latura = None
    latime_latura = None
    raza = None

    def __init__(self, a, b, c):
        self.lungime_latura  = a
        self.latime_latura = b
        self.raza = c

    def printeaz_Lungimea(self):
        print(f'lungimea este {self.lungime_latura}')