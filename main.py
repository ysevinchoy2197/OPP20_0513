# 10-misol
class Stadion:
    def __init__(self, nomi, muxlislar):
        self.nomi = nomi
        self.muxlislar = muxlislar

    def kirish(self, n):
        self.muxlislar += n

    def chiqish(self, n):
        self.muxlislar -= n

    def info(self):
        print(self.nomi, self.muxlislar)
s1 = Stadion("mvtgtekl;", "voi;adn")
s1.info()
