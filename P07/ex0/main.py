from ex0.CreatureCard import CreatureCard
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")

    print("\nTesting Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    try:
        card = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)

        print(card.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"Playable: {card.is_playable(6)}")
        print(f"Play result: {card.play({'mana': 6})}")

        print("\nFire Dragon attacks Goblin Warrior:")
        target = CreatureCard("Goblin Warrior", 2, "common", 2, 3)

        print(f"Attack result: {card.attack_target(target)}")

        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {card.is_playable(3)}")

        print("\nAbstract pattern successfully demonstrated!")
    except ValueError as e:
        print(e)
