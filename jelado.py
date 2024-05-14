class Adat:
    def __init__(self, ora, perc, mperc, x, y):
        self.ora = int(ora)
        self.perc = int(perc)
        self.mperc = int(mperc)
        self.x = x
        self.y = y

    def __str__(self):
        return f'Óra: {self.ora} \nPerc: {self.perc} \nMásodperc: {self.mperc} \nX: {self.x} \nY: {self.y}'
    
    def mpbe(self):
        return int((self.ora * 3600) + (self.perc * 60) + self.mperc)

def eltelt(kezd, veg):
    return int(veg - kezd)

f = open('jel.txt', 'rt', encoding='UTF-8')

lista = []
for sor in f:
    sor = sor.strip().split(' ')
    lista.append(Adat(int(sor[0]), int(sor[1]), int(sor[2]), int(sor[3]), int(sor[4])))

print('2. feladat')
beker = int(input('Adja meg a jel sorszámát! ')) - 1

print(f'x={lista[beker].x} y={lista[beker].y}')



teljes = eltelt(lista[0].mpbe(), lista[len(lista) - 1].mpbe())



print('4. feladat')

print(f'Időtartam: {int(teljes / 3600)}:{int((teljes % 3600/60))}:{(teljes % 3600 %60)}')