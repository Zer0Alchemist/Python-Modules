from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        found = False
        for n in self.crew:
            if n.rank is Rank.COMMANDER or n.rank is Rank.CAPTAIN:
                found = True
        if found is False:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            exp = []
            for n in self.crew:
                if n.years_experience >= 5:
                    exp.append(n)
            if len(exp) < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) "
                                 "need 50% experienced crew (5+ years)")
        for n in self.crew:
            if n.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        sarah = CrewMember(member_id="SARAH_01", name="Sarah Connor",
                           rank=Rank.COMMANDER, age=40,
                           specialization="Mission Command",
                           years_experience=20)
        john = CrewMember(member_id="JOHN_01", name="John Smith",
                          rank=Rank.LIEUTENANT,
                          age=30, specialization="Navigation",
                          years_experience=7)
        alice = CrewMember(member_id="ALICE_01", name="Alice Johnson",
                           rank=Rank.OFFICER,
                           age=23, specialization="Engineering",
                           years_experience=3)
        mars = SpaceMission(mission_id="M2024_MARS",
                            mission_name="Mars Colony Establishment",
                            destination="Mars",
                            duration_days=900, crew=[sarah, john, alice],
                            budget_millions=2500.0,
                            launch_date="2026-09-02T13:00:00")
        print(f"Mission: {mars.mission_name}")
        print(f"ID: {mars.mission_id}")
        print(f"Destination: {mars.destination}")
        print(f"Duration: ${mars.duration_days} days")
        print(f"Budget: ${mars.budget_millions}M")
        print(f"Crew size: {len(mars.crew)}")
        print("Crew members:")
        print(f"- {sarah.name} ({sarah.rank.value}) - {sarah.specialization}")
        print(f"- {john.name} ({john.rank.value}) - {john.specialization}")
        print(f"- {alice.name} ({alice.rank.value}) - {alice.specialization}")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        sarah = CrewMember(member_id="SARAH_01", name="Sarah Connor",
                           rank=Rank.OFFICER, age=40,
                           specialization="Mission Command",
                           years_experience=20)
        john = CrewMember(member_id="JOHN_01", name="John Smith",
                          rank=Rank.LIEUTENANT, age=30,
                          specialization="Navigation", years_experience=7)
        alice = CrewMember(member_id="ALICE_01", name="Alice Johnson",
                           rank=Rank.OFFICER, age=23,
                           specialization="Engineering", years_experience=3)
        mars = SpaceMission(mission_id="M2024_MARS",
                            mission_name="Mars Colony Establishment",
                            destination="Mars", duration_days=900,
                            crew=[sarah, john, alice], budget_millions=2500.0,
                            launch_date="2026-09-02T13:00:00")
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
