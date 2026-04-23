from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        effects = ["damage", "heal", "buff", "debuff"]
        if effect_type not in effects:
            raise ValueError("Uknown effects!")
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        avail_mana = game_state.get("mana", 0)
        if not self.is_playable(avail_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        if self.effect_type == "damage":
            effects = "Deal damage to target"
        elif self.effect_type == "heal":
            effects = "heal player"
        elif self.effect_type == "buff":
            effects = "buff player"
        elif self.effect_type == "debuff":
            effects = "debuff target"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effects
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "effect": self.effect_type,
            "target": targets,
            "action": f"applied {self.effect_type} to {len(targets)} targets"
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = "spell"
        info["effect_type"] = self.effect_type
        return info
