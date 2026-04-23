import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def func_data(*args) -> str:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time: .3f} seconds")
        return result

    return func_data


@spell_timer
def fireball(*args):
    return "Fireball cast!"


def power_validtor(min_power: int) -> callable:
    def func_valid(func: callable) -> callable:
        @functools.wraps(func)
        def validate(*args) -> str:
            if len(args) > 2:
                power = args[2]
            elif len(args) > 0:
                power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args)

        return validate

    return func_valid


@power_validtor(20)
def powah(power: int) -> str:
    return "kaboosh"


def retry_spell(max_attempts: int) -> callable:
    def func_valid(func: callable) -> callable:
        @functools.wraps(func)
        def attempts(*args):
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return attempts

    return func_valid


@retry_spell(3)
def uppering(string: str) -> str:
    try:
        return f"converrting {string} = {string.upper()}"
    except Exception:
        raise Exception("test")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 or any(x.isnumeric() for x in name):
            return False
        else:
            return True

    @power_validtor(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power}"


if __name__ == "__main__":
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(f"Testing with 10 power: {powah(10)}")
    print(f"Testing with 50 power: {powah(50)}")

    print("\nTesting retry spell...")
    print(f"Result = {uppering('Hello World')}")

    print("\nTesting MageFuild...")
    print(MageGuild.validate_mage_name("Hello World"))
    print(MageGuild.validate_mage_name("ha"))

    spell1 = MageGuild()
    spell2 = MageGuild()
    print(spell1.cast_spell("Lightning", 15))
    print(spell2.cast_spell("test", 5))
