from ex0.Card import Card
import random
from typing import Dict


class Deck:
    def __init__(self) -> None:
        self.cards: list = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for n in self.cards:
            if n.name == card_name:
                self.cards.remove(n)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("ERROR: No cards available!")
        else:
            card = self.cards.pop(0)
            return card

    def get_deck_stats(self) -> Dict:
        le = len(self.cards)
        le_creature = 0
        le_spell = 0
        le_artifact = 0
        total = 0

        for n in self.cards:
            cost = n.get_card_info()
            total += cost["cost"]

        for card in self.cards:
            info = card.get_card_info()
            if info["type"] == "creature":
                le_creature += 1
            if info["type"] == "spell":
                le_spell += 1
            if info["type"] == "artifact":
                le_artifact += 1

        return {
            "total_cards": le,
            "creatures": le_creature,
            "spells": le_spell,
            "artifacts": le_artifact,
            "avg_cost": f"{(total / le): .2f}"
        }
