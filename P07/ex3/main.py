from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.get_factorycard_name()}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    print(f"Hand: {result['hand']}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    creature = factory.create_creature(None)
    creat = factory.create_creature(5)
    enemy = factory.create_creature("sbe33")

    engine_update = engine.simulate_turn()
    print(f"actions: {strategy.execute_turn([creature, creat], [enemy])}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
