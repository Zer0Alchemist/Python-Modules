from ex2.EliteCard import EliteCard
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    card = ["play", "get_card_info", "is_playable"]
    combatable = ["attack", "defend", "get_combat_stats"]
    magical = ["cast_spell", "channel_mana", "get_magic_stats"]

    print(f"- Card: {card}")
    print(f"- Combatable: {combatable}")
    print(f"- Magical: {magical}")

    print("\nPlaying Arcane Warrior (Elite  Card):\n")

    print("Combat phase:")
    try:
        attacker = EliteCard("Arcane_Warrior", 4, Rarity.RARE.value, 5, 3,
                             8, 10, "melee")
        enemy1 = EliteCard("Enemy1", 7, Rarity.COMMON.value, 5, 2, 3, 2, "gun")
        enemy2 = EliteCard("Enemy2", 6, Rarity.UNCOMMON.value, 8, 3, 1, 4,
                           "stick")

        print(f"Attack result: {attacker.attack(enemy1)}")
        print(f"Defense result: {attacker.defend(5)}")

        print("\nMagic phase:")
        print("Spell cast: "
              f"{attacker.cast_spell('Fireball', [enemy1.name, enemy2.name])}")
        print(f"Mana channel: {attacker.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except ValueError as e:
        print(e)
