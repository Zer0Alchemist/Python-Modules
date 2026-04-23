if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_hunter', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_hunter',
        'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique = alice.union(bob, charlie)
    lenght = len(unique)

    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {lenght}\n")

    common = alice.intersection(bob, charlie)
    rare_bob = bob.difference(alice, charlie)
    rare_charlie = charlie.difference(alice, bob)
    rare = rare_bob | rare_charlie

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    common_bob_alice = alice.intersection(bob)
    unique_alice = alice.difference(bob)
    unique_bob = bob.difference(alice)

    print(f"Alice vs Bob common: {common_bob_alice}")
    print(f"Alice unique: {unique_alice}")
    print(f"Bob unique: {unique_bob}")
