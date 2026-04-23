from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type is ContactType.PHYSICAL:
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type is ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Telephatic contact requires "
                                 "at least 3 witnesses")
        if self.signal_strength > 7.0:
            if not isinstance(self.message_received, str):
                raise ValueError("Strong signals (7.0) should include "
                                 "recieved messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    print("Valid contact report:")
    try:
        stion = AlienContact(contact_id="AC_2024_001",
                             location="Area 51, Nevada",
                             contact_type=ContactType.RADIO.value,
                             signal_strength=8.5, duration_minutes=45,
                             witness_count=5,
                             message_received="Greetings from Zeta Reticuli",
                             timestamp="2027-06-12T14:30:00")
        print(f"ID: {stion.contact_id}")
        print(f"Type: {stion.contact_type.value}")
        print(f"Location: {stion.location}")
        print(f"Signal: {stion.signal_strength}/10")
        print(f"Duration: {stion.duration_minutes} minutes")
        print(f"Witnesses: {stion.witness_count}")
        print(f"Message: '{stion.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    print()

    print("======================================")
    print("Expected validation error:")
    try:
        stion = AlienContact(contact_id="AC_2024_001",
                             location="Area 51, Nevada",
                             contact_type=ContactType.TELEPATHIC.value,
                             signal_strength=8.5, duration_minutes=45,
                             witness_count=1,
                             message_received="Greetings from Zeta Reticuli",
                             timestamp="2027-06-12T14:30:00")
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
