class father:
    behavior = "confident"
    def __init__(self, name):
        self.name = name

class Daughter(father):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

MrOgwang = father("Ogwang")
Joana = Daughter(19,"female")
print(Joana.behavior)
                