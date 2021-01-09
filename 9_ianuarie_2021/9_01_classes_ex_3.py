
class Card():
    def __init__(self, card_type, attack=2, defense=4):
        self.card_type = card_type
        self.attack = attack
        self.defense = defense


class Player():
    def __init__(self, name="User"):
        self.name = name
        self.cards = []

    def total_attack(self):
        return sum([card.attack for card in self.cards])

    def total_defense(self):
        return sum([card.defense for card in self.cards])

    def fight(self, opponent):
        if self.total_attack() > opponent.total_defense():
            return f"{self.name} wins! It has a total attack of {self.total_attack()} while {opponent.name} has a total defense of {opponent.total_defense()}."
        elif self.total_attack() < opponent.total_defense():
            return f"{self.name} loses! It has a total attack of {self.total_attack()} while {opponent.name} has a total defense of {opponent.total_defense()}."
        else:
            return "It's a draw!"


    

elf = Card("elf")
goblin = Card("goblin", attack=5, defense=1)

player1 = Player("User1")
player2 = Player("User2")

for i in range(3):
    player1.cards.append(elf)
    player2.cards.append(goblin)

for i in range(2):
    player1.cards.append(goblin)
    player2.cards.append(elf)

print("")
print(player1.fight(player2))
print("")
print(player2.fight(player1))