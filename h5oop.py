class hesap:
    def __init__(self,say1,say2):
        self.say1 = say1
        self.say2 = say2
    def carp(self):
        sonuc = self.say1 * self.say2
        return sonuc
    def bol(self):
        sonuc = self.say1 / self.say2
        return sonuc
    def topla(self):
        sonuc = self.say1 + self.say2
        return sonuc
    def cıkar(self):
        sonuc = self.say1 - self.say2
        return sonuc
    def yazdir(self):
        print(self.bol())
        print(self.topla())
        print(self.cıkar())


A = hesap(5, 3)
A.yazdir()


