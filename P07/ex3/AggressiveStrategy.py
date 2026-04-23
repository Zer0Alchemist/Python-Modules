from ex3.GameStrategy import GameStrategy
from typing import Dict, List


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> Dict:
        cards = []
        mana_used = 0
        dmg_used = 0

        sorted_hand = list(hand)
        for i in range(len(sorted_hand)):
            for j in range(0, len(sorted_hand) - i - 1):
                if sorted_hand[j].cost > sorted_hand[j + 1].cost:
                    temp = sorted_hand[j]
                    sorted_hand[j] = sorted_hand[j + 1]
                    sorted_hand[j + 1] = temp

        for card in sorted_hand:
            cards.append(card.name)
            mana_used += card.cost
            dmg_used += getattr(card, "atk", 0)

        for card in battlefield:
            dmg_used += getattr(card, "atk", 0)

        targets = self.prioritize_targets(["Enemy Creature", "Enemy Player"])

        return {
            "cards_played": cards,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": dmg_used
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> List:
        return available_targets
