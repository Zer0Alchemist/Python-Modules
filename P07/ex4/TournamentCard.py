from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 atk: int, defense: int, hp: int, idd: str, rating: int,
                 combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        if cost <= 0 or atk < 0 or defense < 0 or hp < 0:
            raise ValueError("ERROR: all key ints must be positive ints")
        self.atk = atk
        self.defense = defense
        self.hp = hp
        self.idd = idd
        self.combat_type = combat_type
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> Dict:
        avail_mana = game_state.get("mana", 0)
        if not self.is_playable(avail_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        else:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned into the battlefield"
            }

    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.atk,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict:
        dmg_taken = max(0, incoming_damage - self.defense)
        dmg_blocked = max(0, incoming_damage - dmg_taken)
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
            "name": self.name,
            "attack_stat": self.atk,
            "attack_tool": self.combat_type,
            "defense_stat": self.defense,
            "hp": self.hp
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += 1
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += 1
        self.rating = max(0, self.rating - 16)

    def get_rank_info(self) -> Dict:
        return {
            "Interfaces": ["Card", "Combatable", "Rankable"],
            "Rating": self.rating,
            "Record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "name": self.name,
            "ID": self.idd,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "win-loss": f"{self.wins}-{self.losses}"
        }
