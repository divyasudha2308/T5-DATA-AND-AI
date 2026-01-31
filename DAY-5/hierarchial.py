class Mother:
    def cook(self):
        print("mother cooks well")
class Daughter(Mother):
    def dance(self):
        print("daughter can dance")
class Son(Mother):
    def play(self):
        print("son can play")

s=Son()
d=Daughter()
s.cook()
d.cook()
d.dance()
s.play()
