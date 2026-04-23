from ex4.TournamentCard import TournamentCard
from typing import Dict
import random


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.idd] = card
        return card.idd

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        cards = [card1_id, card2_id]

        winner = random.choice(cards)
        if winner == card1_id:
            loser = card2_id
        elif winner == card2_id:
            loser = card1_id

        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)

        winner_rating = self.cards[winner].calculate_rating()
        loser_rating = self.cards[loser].calculate_rating()
        self.matches += 1
        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": winner_rating,
            "loser_rating": loser_rating
        }

    def get_leaderboard(self) -> list:
        rate = list(self.cards.values())

        for i in range(len(self.cards)):
            for j in range(0, len(self.cards) - i - 1):
                if rate[j].rating < rate[j + 1].rating:
                    temp = rate[j]
                    rate[j] = rate[j + 1]
                    rate[j + 1] = temp

        rank = []
        ranking = 1
        for n in rate:
            rank.append(f"{ranking}. {n.name} - Rating: "
                        f"{n.rating} ({n.wins}-{n.losses})")
            ranking += 1

        return rank

    def generate_tournament_report(self) -> Dict:
        card = list(self.cards.values())
        if len(card) == 0:
            avg = 0
        else:
            avg = sum(c.rating for c in card) / len(card)

        if self.matches == 0 or len(self.cards.values()) == 0:
            return {
                "total_cards": len(self.cards),
                "matches_played": self.matches,
                "avg_rating": avg,
                "platform_status": "inactive"
            }
        else:
            return {
                "total_cards": len(self.cards),
                "matches_played": self.matches,
                "avg_rating": avg,
                "platform_status": "active"
            }
