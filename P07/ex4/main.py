from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")

    try:
        print("Registering Tournament Cards...\n")

        dragon = TournamentCard("Fire Dragon", 7, Rarity.LEGENDARY.value, 6, 5,
                                10, "dragon_001", 1200, "Fire")
        wizard = TournamentCard("Ice Wizard", 5, Rarity.RARE.value, 5, 6, 8,
                                "wizard_001", 1150, "Melee")
        platform = TournamentPlatform()
        dragon_id = platform.register_card(dragon)
        wizard_id = platform.register_card(wizard)
        dragon_info = dragon.get_rank_info()
        wizard_info = wizard.get_rank_info()

        print(f"{dragon.name} (ID: {dragon_id}):")
        print(f"- Interfaces: {dragon_info['Interfaces']}")
        print(f"- Rating: {dragon_info['Rating']}")
        print(f"- Record: {dragon_info['Record']}")

        print(f"\n{wizard.name} (ID: {wizard_id}):")
        print(f"- Interfaces: {wizard_info['Interfaces']}")
        print(f"- Rating: {wizard_info['Rating']}")
        print(f"- Record: {wizard_info['Record']}")

        print("\n Creating tournamnt match...")
        print(f"Match result: {platform.create_match(dragon_id, wizard_id)}")

        print("\ntournament Leaderboard:")
        rankings = platform.get_leaderboard()
        for rank in rankings:
            print(rank)

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deploted! ===")
        print("All abstract patterns working together harmoniously!")
    except ValueError as e:
        print(e)
