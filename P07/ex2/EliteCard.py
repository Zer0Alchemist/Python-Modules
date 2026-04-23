from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 atk: int, deff: int, mana: int, hp: int,
                 comb_type: str) -> None:
        super().__init__(name, cost, rarity)
        if atk <= 0 or deff <= 0 or mana <= 0 or hp <= 0:
            raise ValueError("ERROR: HP, Att, Def, Mana must "
                             "take positive ints")
        self.atk = atk
        self.deff = deff
        self.mana = mana
        self.hp = hp
        self.comb_type = comb_type

    def play(self, game_state: dict) -> Dict:
        avail_mana = game_state.get("mana", 0)
        if not self.is_playable(avail_mana):
            return {
                "card_played": self.name,
                "cost": 0,
                "action": "Not enough mana"
            }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "action": "summoned into the battlefield"
        }

    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.atk,
            "combat_type": self.comb_type
        }

    def defend(self, incoming_damage: int) -> Dict:
        dmg_taken = max(0, incoming_damage - self.deff)
        dmg_blocked = incoming_damage - dmg_taken
        self.hp -= dmg_taken

        if self.hp <= 0:
            alive = False
        else:
            alive = True
        return {
            "defender": self.name,
            "damage_taken": dmg_taken,
            "damage_blocked": dmg_blocked,
            "still_alive": alive
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack_stats": self.atk,
            "combat_tool": self.comb_type,
            "defense_stats": self.deff,
            "health": self.hp
        }

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        if self.mana <= 0:
            raise ValueError("ERRROR: Not enough mana")

        mana_used = max(0, self.mana - self.cost)
        self.mana -= self.cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        if amount <= 0:
            raise ValueError("ERROR: Amount must be positive")

        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "spells": "to be decided by attacker",
            "mana": self.mana
        }
