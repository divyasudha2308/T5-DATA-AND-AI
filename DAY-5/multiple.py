class Father:
    def drive(self):
        print("father drives")
class Mother:
    def cook(self):
        print("mother cooks")
class Child(Father,Mother):
    def play(self):
        print("child plays")
c=Child()
c.cook()
c.drive()
c.play()