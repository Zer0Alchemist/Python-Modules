def calculate_value(player: dict):
    total = 0
    for item in player['inventory'].values():
        total += item['count'] * item['value']
    return total


def calculate_count(player: dict):
    total = 0
    for item in player['inventory'].values():
        total += item['count']
    return total


def print_inv(player: dict):
    print(f"=== {player['name']}'s Inventory ===")
    for item_name, data in player['inventory'].items():
        total = data['count'] * data['value']
        print(
            f"{item_name} ({data['types']}, {data['rarity']}): "
            f"{data['count']}x @ {data['value']} gold each = "
            f"{total} gold")


def transfer(player: dict, receiver: dict, name: str, quantity: int):
    if name not in player['inventory']:
        print("Item not found!\n")
        return

    if player['inventory'][name]['count'] < quantity:
        print("Not enough quantity!")
        return

    player['inventory'][name]['count'] -= quantity

    item_check = receiver['inventory'].get(name)
    if item_check is None:
        name_dict = player['inventory'][name]
        item_data = {
            "types": name_dict['types'],
            "rarity": name_dict['rarity'],
            "count": name_dict['count'],
            "value": name_dict['value']
        }
        receiver['inventory'].update({name: item_data})
    else:
        count_now = receiver['inventory'][name]['count'] + quantity
        receiver['inventory'][name].update({'count': count_now})

    print("Transaction successful!\n")


def rarity(player: dict):
    rarities = {
        "common": 0,
        "uncommon": 1,
        "rare": 2,
        "legendary": 3
    }
    rarity = -1
    rare_item = ""
    for base_name, data in player['inventory'].items():
        curr_rank = rarities.get(data['rarity'], -1)
        if curr_rank > rarity and curr_rank >= 2:
            rarity = curr_rank
            rare_item = base_name
    return rare_item


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")

    alice = {
        "name": "Alice",
        "inventory": {
            "sword": {
                "types": "weapon",
                "rarity": "rare",
                "count": 1,
                "value": 500
            },
            "potion": {
                "types": "consumable",
                "rarity": "common",
                "count": 5,
                "value": 50
            },
            "shield": {
                "types": "armor",
                "rarity": "uncommon",
                "count": 1,
                "value": 200
            }
        }
    }
    bob = {
        "name": "Bob",
        "inventory": {
            "potion": {
                "types": "consumable",
                "rarity": "common",
                "count": 0,
                "value": 50
            },
            "magic_ring": {
                "types": "armor",
                "rarity": "legendary",
                "count": 1,
                "value": 350
            }
        }
    }

    print_inv(alice)

    print(f"\nInventory value: {calculate_value(alice)} gold")
    print(f"Item count: {calculate_count(alice)} items")
    cat = dict(alice['inventory'].items())
    print(
        f"Categories: {cat['sword']['types']}({cat['sword']['count']}), "
        f"{cat['potion']['types']}({cat['potion']['count']}), "
        f"{cat['shield']['types']}({cat['shield']['count']})\n")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    transfer(alice, bob, "potion", 2)

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice['inventory']['potion']['count']}")
    print(f"Bob potions: {bob['inventory']['potion']['count']}\n")

    print("=== Inventory Analytics ===")
    if calculate_value(alice) > calculate_value(bob):
        print(
            f"Most valuable player: {alice['name']} "
            f"({calculate_value(alice)} gold)")
    else:
        print(
            f"Most valuable player: {bob['name']} "
            f"({calculate_value(bob)} gold)")
    if calculate_count(alice) > calculate_count(bob):
        print(f"Most items: {alice['name']} ({calculate_count(alice)} items)")
    else:
        print(f"Most items: {bob['name']} ({calculate_count(bob)} items)")

    rarest_al = rarity(alice)
    rarest_bob = rarity(bob)
    print(f"rarest items: {rarest_al} {rarest_bob}")
