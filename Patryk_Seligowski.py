class Mac_2d_k:
    wys: int
    szer: int
    dane: list[list[float]]
    def __init__(self):
        self.dane = []
        self.wys = 0
        self.szer = 0

    def ustal(self, nr_wiersza: int, nr_kolumny: int, wartosc: float):
        while nr_wiersza > self.wys:
            pom = []
            for i in range(self.szer):
                pom.append(0)
            self.dane.append(pom)
            self.wys += 1
        while nr_kolumny > self.szer:
            for i in range(self.wys):
                self.dane[i].append(0)
            self.szer += 1

        self.dane[nr_wiersza-1][nr_kolumny-1] = wartosc

    def print(self):
        for i in range(self.wys):
            pom = []
            for j in range(self.szer):
                pom.append(self.dane[i][j])
            print(pom)
        print()

    def pobierz(self, nr_wiersza: int, nr_kolumny: int):
        if self.wys < nr_wiersza:
            return 0
        elif self.szer < nr_kolumny:
            return 0
        else:
            return self.dane[nr_wiersza-1][nr_kolumny-1]

    def transponuj(self):
        temp = Mac_2d_k()
        for x in range(self.wys):
            for y in range(self.szer):
                temp.ustal(y+1, x+1, self.dane[x][y])
        return temp

    def uprosc(self):
        x = 0
        y = 0
        for i in range(self.wys):
            for j in range(self.szer):
                if self.dane[i][j] > 0:
                    if j > x:
                        x = j
                    if i > y:
                        y = i

        for i in reversed(range(y+1, self.wys)):
            for j in reversed(range(x+1, self.szer)):
                self.dane[i].pop(j)
                self.szer -= 1

        for i in reversed(range(y+1, self.wys)):
            self.dane.pop(i)
            self.wys -= 1

    def mnozenie(self, macierz):
        temp = Mac_2d_k()
        temp.ustal(self.wys, self.szer, 0)
        for i in range(self.szer):
            for j in range(self.szer):
                for k in range(self.szer):
                    temp.ustal(i, j, temp.pobierz(i+1, j+1) + self.dane[i-1][k-1] * macierz.pobierz(k+1, j+1))
        return temp

object = Mac_2d_k()
object.ustal(3, 4, 1)
object.ustal(1, 1, 1)

object.print()
print(object.pobierz(1, 1))
transponowany = object.transponuj()
transponowany.print()
object.ustal(6, 6, 0)
object.ustal(4, 3, 2)
object.print()
object.uprosc()
object.print()

## Pełne macierze
print("mnoz")
object2= Mac_2d_k()
object.ustal(1, 1, 1)
object.ustal(2, 1, 2)
object.ustal(3, 1, 1)
object.ustal(4, 1, 1)
object.ustal(1, 2, 1)
object.ustal(2, 2, 2)
object.ustal(3, 2, 1)
object.ustal(4, 2, 1)
object.ustal(1, 3, 1)
object.ustal(2, 3, 2)
object.ustal(3, 3, 1)
object.ustal(4, 3, 1)
object.ustal(1, 4, 1)
object.ustal(2, 4, 2)
object.ustal(3, 4, 1)
object.ustal(4, 4, 1)
object2.ustal(1, 1, 1)
object2.ustal(2, 1, 2)
object2.ustal(3, 1, 1)
object2.ustal(4, 1, 1)
object2.ustal(1, 2, 1)
object2.ustal(2, 2, 2)
object2.ustal(3, 2, 1)
object2.ustal(4, 2, 1)
object2.ustal(1, 3, 1)
object2.ustal(2, 3, 2)
object2.ustal(3, 3, 1)
object2.ustal(4, 3, 1)
object2.ustal(1, 4, 1)
object2.ustal(2, 4, 2)
object2.ustal(3, 4, 1)
object2.ustal(4, 4, 1)
mnoz = object.mnozenie(object2)
mnoz.print()


