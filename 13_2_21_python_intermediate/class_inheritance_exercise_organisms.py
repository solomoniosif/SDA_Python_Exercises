""" TODO: Scrieti o iererhie de clase care sa includa urmatoarele clase de animale:
unicelulare, multicelulare, vertebrate, nevertebrate, pesti, mamifere, pasari, serpi, soparle, gandaci, parameci.
Bonus: adaugati o interfata audio pentru metodele noastre"""

from abc import abstractmethod


class Organism:
    def __init__(self, name):
        self.name = name

    @property
    def is_alive(self):
        return True


class Prokaryote(Organism):
    def __init__(self, name):
        super().__init__(name)

    @property
    def enclosed_cell_nucleus(self):
        return False

    @property
    def sexual_reproduction(self):
        return False


class Eukaryote(Organism):
    def __init__(self, name):
        self.name = name

    @property
    def enclosed_cell_nucleus(self):
        return True


class Unicellular(Organism):
    def __init__(self, name):
        super().__init__(name)

    @property
    def one_cell_organism(self):
        return True


class Multicellular(Organism):
    def __init__(self, name):
        super().__init__(name)

    @property
    def one_cell_organism(self):
        return False


class Animal(Multicellular, Eukaryote):
    def __init__(self, name, sexual_reproduction=True):
        super().__init__(name)
        self.sexual_reproduction = sexual_reproduction

    @property
    def breaths_oxygen(self):
        return True

    @property
    def is_heterotroph(self):
        return True


class Invertebrate(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def has_vertebral_column(self):
        return False


class Vertebrate(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def has_vertebral_column(self):
        return True


class Reptile(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

    @property
    def is_warm_blooded(self):
        return False


class Fish(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

    @property
    def breaths_underwater(self):
        return True

    @property
    def is_warm_blooded(self):
        return False


class Bird(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

    @property
    def is_warm_blooded(self):
        return True

    @property
    def has_wings(self):
        return True

    @property
    def is_oviparous(self):
        return True


class Snake(Reptile):
    def __init__(self, name, is_oviparous=True):
        super().__init__(name)
        self.is_oviparous = is_oviparous

    @property
    def has_limbs(self):
        return False


class Lizard(Reptile):
    def __init__(self, name, is_oviparous=True):
        super().__init__(name)
        self.is_oviparous = is_oviparous

    @property
    def has_limbs(self):
        return True


class Insect(Invertebrate):
    def __init__(self, name):
        super().__init__(name)


class Beetle(Insect):
    def __init__(self, name):
        super().__init__(name)


class Paramecium(Unicellular, Eukaryote):
    def __init__(self, name):
        super().__init__(name)


class Mammal(Vertebrate):
    def __init__(self, name):
        super().__init__(name)

    @property
    def is_warm_blooded(self):
        return True


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name)


def get_all_superclasses(org_class):
    superclasses = []
    for superclass in org_class.mro()[1:-1]:
        superclasses.append(superclass.__name__)
    return ', '.join(superclasses)


organisms = [Paramecium, Eukaryote, Multicellular, Animal, Beetle, Bird, Fish, Snake, Lizard, Human]

for organism in organisms:
    print(f"All superclasses of {organism.__name__}: {get_all_superclasses(organism)}.")

animals = [organism.__name__ for organism in organisms if issubclass(organism, Animal)]

print(animals)
