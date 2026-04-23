from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 atk: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if atk <= 0 or health <= 0:
            raise ValueError(
                f"ERROR: {self.name} ATT and HP must be positive ints!")
        self.atk = atk
        self.health = health

    def play(self, game_state: dict) -> Dict:
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
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.atk,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = "creature"
        info["attack"] = self.atk
        info["health"] = self.health
        return info
