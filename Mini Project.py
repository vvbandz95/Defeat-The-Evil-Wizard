import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Attack on {opponent.name} for {damage} damage!")

    def shield_block(self):
        print(f"{self.name} blocks the next attack!")
        return True

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        damage = random.randint(30, 50)
        opponent.health -= damage
        print(f"{self.name} casts a spell on {opponent.name} for {damage} damage!")

    def mana_shield(self):
        print(f"{self.name} uses Mana Shield and takes no damage this turn!")
        return True

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def quick_shot(self, opponent):
        damage = random.randint(15, 25) * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def evade(self):
        print(f"{self.name} evades the next attack!")
        return True

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def holy_strike(self, opponent):
        damage = random.randint(20, 40)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        print(f"{self.name} uses Divine Shield and blocks the next attack!")
        return True

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen_amount = random.randint(5, 15)
        self.health += regen_amount
        print(f"{self.name} regenerates {regen_amount} health! Current health: {self.health}/{self.max_health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        if wizard.health > 0:
            print("\n--- Evil Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()
