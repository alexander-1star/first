class Grandparent:
    height = 150
    hair = 'brown'
    eyes = 'hazel'
    def __init__(self):


class Parent(Grandparent):
    height = 220
    hair = 'brown'
    eye = ' blue'


class Child(Parent):
    eyes = 'green'
    def __init__(self):
        print(self.height)
        print(self.hair)
        print(self.eyes)
