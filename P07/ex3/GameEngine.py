from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Dict


class GameEngine:
    def __init__(self):
        self.turn = 0
        self.dmg = 0
        self.cards = 0
        self.factory = None
        self.strategy = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if self.factory is None or self.strategy is None:
            raise ValueError("Engine not configured!")

        hand = [
            self.factory.create_creature(),
            self.factory.create_spell(),
            self.factory.create_artifact()]

        result = self.strategy.execute_turn(hand, [])

        self.turn += 1
        self.dmg += result["damage_dealt"]
        self.cards += len(hand)

        card_info = []
        for card in hand:
            card_info.append(f"{card.name} ({card.cost})")

        return {
            "hand": card_info,
            "strategy": self.strategy.get_strategy_name(),
            "actions": result
        }

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.dmg,
            "cards_created": self.cards
        }
