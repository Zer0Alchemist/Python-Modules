from typing import List, Dict
import functools
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return functools.reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise Exception("ERROR: Invalid operation")


def enchant_base(power: int, element: str, target: str) -> str:
    return f"{element} enchantment did a {power} power hit to {target}"


def partial_enchanter(base_enchantment: callable) -> Dict[str, callable]:
    fire = functools.partial(enchant_base, power=50, element="fire")
    ice = functools.partial(enchant_base, power=50, element="ice")
    lightning = functools.partial(enchant_base, power=50,
                                  element="lightning")
    return {
            "fire_enchant": fire,
            "ice_enchant": ice,
            "lightning_enchant": lightning
        }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def spell(arg) -> str:
        return "Uknown spell type"

    @spell.register(int)
    def dmg_spell(arg: int) -> str:
        return f"spell did {arg} damage"

    @spell.register(str)
    def enchantment(arg: str) -> str:
        return f"A {arg} has been put to the spell"

    @spell.register(list)
    def multi_cast(arg: List) -> str:
        return f"Spell casts are: {arg}"

    return spell


if __name__ == "__main__":
    try:
        print("\nTesting spell reducer...")
        summ = spell_reducer([25, 25, 30, 20], "add")
        print(f"Sum: {summ}")

        product = spell_reducer([2000, 12], "multiply")
        print(f"Product: {product}")

        maxx = spell_reducer([21, 40, 30, 6, 7, 22, 32], "max")
        print(f"Max: {maxx}")

        print("\nTesting partial enchanter...")
        p_ench = partial_enchanter(enchant_base)
        print(f"{p_ench['fire_enchant'](target='Lion Crusher')}")
        print(f"{p_ench['ice_enchant'](power=20, target='Goblin slayer')}")
        print(f"{p_ench['lightning_enchant'](power=100, target='Natenyahu')}")

        print("\nTesting memoized fibonacci...")
        fib = memoized_fibonacci(10)
        print(f"Fib(10): {fib}")
        fib = memoized_fibonacci(15)
        print(f"Fib(15): {fib}")

        print("\nTesting spell dispatcher...")
        spell_cast = spell_dispatcher()
        print(f"Damage type test: {spell_cast(20)}")
        print(f"Enchantment test: {spell_cast('UNBREAKING IV')}")
        print(f"Multi cast test: {spell_cast(['lightning road', 'Acheron'])}")
        print(f"Uknown type test: {spell_cast({'skibiddi sigma'})}")
    except Exception as e:
        print(e)
