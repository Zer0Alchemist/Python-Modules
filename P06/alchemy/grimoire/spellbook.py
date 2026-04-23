def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    check = validate_ingredients(ingredients)
    check_valid = check.split(" ")
    if check_valid[1] == "VALID":
        return f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
    else:
        return f"Spell rejected: {spell_name} ({validate_ingredients(ingredients)})"
