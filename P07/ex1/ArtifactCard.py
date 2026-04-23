from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("ERROR: Durability must be positive int!")
        self.durability = durability
        self.effect = effect

    def play(self, game_state) -> Dict:
        avail_mana = game_state.get("mana", 0)
        if not self.is_playable(avail_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict:
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": f"count = {self.durability}"
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = "artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
