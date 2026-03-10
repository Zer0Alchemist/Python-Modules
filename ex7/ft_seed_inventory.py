def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cap = seed_type.capitalize()
    if unit == "packets":
        print(f"{cap} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{cap} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{cap} seeds: covers {quantity} square meters")
    else:
        print("Uknown unit type")
