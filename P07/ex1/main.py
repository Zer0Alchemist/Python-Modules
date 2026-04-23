from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    try:
        creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        spell = SpellCard("Lightning Bolt", 3, Rarity.UNCOMMON.value, "damage")
        artifact = ArtifactCard("Mana Crystal", 2, Rarity.COMMON.value, 4,
                                "+1 mana per turn")

        deck.add_card(creature)
        deck.add_card(spell)
        deck.add_card(artifact)

        print(f"Deck stats: {deck.get_deck_stats()}")

        print("\nDrawing and playing cards:\n")

        print("Drew: Lightning Bolt (Spell)")
        print(f"Play result: {spell.play({'mana': 6})}")

        print("\nDrew: Mana Crystal (Artifact)")
        print(f"Play result: {artifact.play({'mana': 6})}")

        print("\nDrew: Fire Dragon (Creature)")
        print(f"Play result: {creature.play({'mana': 6})}")

        print("\nPolymorphism in action: Same interface,"
              "different card behaviors!")
    except ValueError as e:
        print(e)
