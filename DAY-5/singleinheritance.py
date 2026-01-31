class father:
    def drive(self):
        print("father can drive")
class son(father):
    def play(self):
        print("son is playing")

s=son()
s.drive()
s.play()