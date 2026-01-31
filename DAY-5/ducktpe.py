class Pycharm:
    def execute(self):
        print("compiling + running")
class VScode:
    def execute(self):
        print("running + linting")
def code(editor):
    editor.execute()
code(Pycharm())
code(VScode())