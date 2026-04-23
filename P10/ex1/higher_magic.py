from typing import List


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if not callable(spell1) or not callable(spell2):
        raise Exception("ERROR: function must be callable")
    else:
        return lambda *a: (spell1(*a), spell2(*a))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if not callable(base_spell):
        raise Exception("ERROR: function must be callable")
    else:
        return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not callable(condition) or not callable(spell):
        raise Exception("ERROR: function must be called")
    return lambda *a: spell(*a) if condition(*a) else "Spell fizzled"


def spell_sequence(spells: List[callable]) -> callable:
    for n in spells:
        if not callable(n):
            raise Exception("ERROR: function must be called")
    return lambda *a: [n(*a) for n in spells]


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def fireball_dmg() -> int:
    return 10


def heal(target: str) -> str:
    return f"Heals {target}"


def condition(target: str) -> bool:
    return True


if __name__ == "__main__":
    try:
        print("\nTesting spell combiner...")
        combined = spell_combiner(fireball, heal)
        apply = combined("Dragon")
        print(f"Combined spell result: {apply[0]}, {apply[1]}")

        print("\nTesting power amplifier...")
        mega_fireball = power_amplifier(fireball_dmg, 3)
        amplify = mega_fireball()
        print(f"Original: {fireball_dmg()}, Amplified: {amplify}")

        print("\ntesting conditional caster...")
        spell_cond = conditional_caster(condition, fireball)
        apply_spell = spell_cond("Dragon")
        print(f"Can be applied ({condition('Dragon')}): {apply_spell}")

        print("\ntesting spell sequence...")
        spells = [fireball, heal]
        spell_seq = spell_sequence(spells)
        spell_lst = spell_seq("Dragon")
        for spell in spell_lst:
            print(f"{spell}")
    except Exception as e:
        print(e)
