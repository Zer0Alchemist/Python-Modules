from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Dict
from ex0.Card import Card
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            return CreatureCard(name, 4, Rarity.RARE.value, 2, 10)
        elif isinstance(name_or_power, int):
            power = name_or_power
            return CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value,
                                power, 10)
        else:
            return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value,
                                5, 10)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            return SpellCard(name, 5, Rarity.RARE.value, "buff")
        elif isinstance(name_or_power, int):
            power = name_or_power
            return SpellCard("Fireball", power, Rarity.LEGENDARY.value,
                             "damage")
        else:
            return SpellCard("Healing Light", 4, Rarity.RARE.value, "heal")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            return ArtifactCard(name, 3, Rarity.COMMON.value, 6,
                                "+1 mana per turn")
        elif isinstance(name_or_power, int):
            power = name_or_power
            return ArtifactCard("Dragon Staff", 5, Rarity.RARE.value, power,
                                "+2 attack to all creatures")
        else:
            return ArtifactCard("Crystal orb", 7, Rarity.LEGENDARY.value, 5,
                                "triple spell damage")

    def create_themed_deck(self, size: int) -> Dict:
        creatures = []
        spells = []
        artifacts = []

        for n in range(size // 3):
            creatures.append(self.create_creature())
            spells.append(self.create_spell())
            artifacts.append(self.create_artifact())

        return {
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "total": len(creatures) + len(spells) + len(artifacts)
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "healing light"],
            "artifacts": ["dragon staff", "crystal orb"]
        }

    def get_factorycard_name(self) -> str:
        return "FantasyCardFactory"
