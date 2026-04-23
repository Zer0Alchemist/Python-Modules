from typing import Dict


def mage_counter() -> callable:
    count = 0

    def counting() -> int:
        nonlocal count
        count += 1
        return count

    return counting


def spell_accumulator(initial_power: int) -> callable:
    def counting(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power

    return counting


def enchantment_factory(enchantment_type: str) -> callable:
    def name(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return name


def memory_vault() -> Dict[str, callable]:
    vault = {}

    def store(key: str, value: any) -> None:
        vault[key] = value

    def recall(key: str) -> any:
        if key not in vault.keys():
            return "Memory not found"
        else:
            return vault[key]

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    try:
        print("\nTesting mage counter...")

        count_mage = mage_counter()
        for i in range(1, 4):
            print(f"Call {i}: {count_mage()}")

        print("\nTesting spell accumulator...")

        spell_acc = spell_accumulator(60)
        print(spell_acc(7))
        print(spell_acc(2))
        print(spell_acc(351))
        print("\nTesting enchantment factory...")

        ench_table1 = enchantment_factory("Flaming")
        ench_table2 = enchantment_factory("Frozen")
        print(ench_table1("Sword"))
        print(ench_table2("Shield"))

        print("\nTesting memory vault...")

        vault = memory_vault()
        lol = vault['store']("demon", "bloodbath")
        print(f"{vault['recall']('demon')}")
    except Exception as e:
        print(e)
