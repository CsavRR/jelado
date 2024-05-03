class Adat:
    def __init__(self, ora, perc, mperc, x, y):
        self.ora = ora
        self.perc = perc
        self.mperc = mperc
        self.x = x
        self.y = y

    def __str__(self):
        return f'Óra: {self.ora} \nPerc: {self.perc} \nMásodperc: {self.mperc} \nX: {self.x} \nY: {self.y}'
    
f = open('jel.txt', 'rt', encoding='UTF-8')
f.readline()

lista = []
for sor in f:
    sor = sor.strip().split(' ')
    lista.append(Adat(sor[0], sor[1], sor[2], sor[3], sor[4]))

