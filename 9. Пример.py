import random

class Base:
    base = 10
    @classmethod
    def get_random(cls):
        return random.random() * cls.base

print(Base.get_random())

class NewRandom(Base):
    pass

NewRandom.base = 1
print(NewRandom.get_random())


class NewRandom2(Base):
    @classmethod
    def get_random(cls, a, b):
        return random.randint(a, b)

NewRandom.base = 1
print(NewRandom2.get_random(2, 6))


class NewRandom3(Base):
    @classmethod
    def get_random(cls, a, b):
        value = super().get_random()
        return (value, random.randint(a, b))
        # return super().get_random()

NewRandom.base = 1
print(NewRandom3.get_random(44, 55))
