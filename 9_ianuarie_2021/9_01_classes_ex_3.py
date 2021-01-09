import random


class Card():
    def __init__(self, card_type, attack=2, defense=4):
        self.card_type = card_type
        self.attack = attack
        self.defense = defense

    def __repr__(self):
        return f'{self.card_type}'


class Player():
    def __init__(self, name="User"):
        self.name = name
        self.cards = []
        self.games_won = 0
        self.games_lost = 0

    def total_attack(self):
        return sum([card.attack for card in self.cards])

    def total_defense(self):
        return sum([card.defense for card in self.cards])

    def fight(self, opponent):
        if self.total_attack() > opponent.total_defense():
            self.games_won += 1
            opponent.games_lost += 1
            return f"{self.name} wins! It has a total attack of {self.total_attack()} while {opponent.name} has a total defense of {opponent.total_defense()}."
        elif self.total_attack() < opponent.total_defense():
            self.games_lost += 1
            opponent.games_won += 1
            return f"{self.name} loses! It has a total attack of {self.total_attack()} while {opponent.name} has a total defense of {opponent.total_defense()}."
        else:
            return "It's a draw!"


    
elf = Card("elf")
goblin = Card("goblin", attack=5, defense=1)

player1 = Player("User1")
player2 = Player("User2")



def game():
    for i in range(random.randint(3, 10)):
        player1.cards.append(random.choice([elf, goblin]))
        player2.cards.append(random.choice([elf, goblin]))
    print(player1.fight(player2))
    print(player2.fight(player1))

for i in range(10):
    game()

print(f"{player1.name} won {player1.games_won} games and lost {player1.games_lost}.")
print(f"{player2.name} won {player2.games_won} games and lost {player2.games_lost}.")
