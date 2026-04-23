def validate_ingredients(ingredients: str) -> str:
    valid_keys = ["fire", "water", "earth", "air"]
    ings = ingredients.split()

    for n in ings:
        if n not in valid_keys:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
