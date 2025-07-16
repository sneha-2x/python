class animal():
    def __init__(self,name):
        self.name=name
        print(f'It is {self.name}')
    def live(self):
        pass

#single inheritance
class earth(animal):
    def live(self):
        print(f'{self.name} lives on earth')
        super().live()

#multiple inheritance
class water(animal):
    def live(self):
        print(f'{self.name} lives in water')
        super().live()

#multiple inheritance
class frog(earth,water):
    def live(self):
        super().live()

#multilevel inheritance
class dog(earth):
    def live(self):
        super().live()
    def speak(self):
        print(f'{self.name} barks!')

#hybrid inheritance=any two inheritance combined






a=earth('Dog')
a.live()
b=water('Fish')
b.live()
c=frog('Trok')
c.live()
d=dog('Maddy')
d.live()
d.speak()
