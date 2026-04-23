import alchemy.transmutation.basic
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy.transmutation

if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): [same as above]")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
