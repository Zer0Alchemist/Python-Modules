from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


if __name__ == "__main__":
    print("\n===Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    valid = validate_ingredients("fire air")
    invalid = validate_ingredients("dragon scales")
    print(f"validate_ingredients(\"fire air\"): {valid}")
    print(f"validate_ingredients(\"dragon scales\"): {invalid}")

    print("\nTesting spell recording with validation:")
    val = record_spell("Fireball", "fire air")
    inv = record_spell("Dark Magic", "shadow")
    print(f"record_spell(\"Fireball\", \"fire air\"): {val}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {inv}")

    print("\nTesting late import techniqye:")
    late = record_spell("Lightning", "air")
    print(f"record_spell(\"Lightining\", \"air\"): {late}")

    print("\n Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
