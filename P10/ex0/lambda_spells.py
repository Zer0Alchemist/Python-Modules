from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    s_lst = sorted(artifacts, key=lambda artifacts: artifacts["power"],
                   reverse=True)
    return s_lst


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    f_lst = list(filter(lambda mages: mages["power"] >= min_power,
                        mages))
    return f_lst


def spell_transformer(spells: List[str]) -> List[str]:
    t_lst = list(map(lambda s: f"* {s} *", spells))
    return t_lst


def mage_stats(mages: List[Dict]) -> Dict:
    maxx = max(mages, key=lambda m: m["power"])
    minn = min(mages, key=lambda n: n["power"])
    summ = sum(map(lambda x: x['power'], mages))
    avg = float(summ / len(mages))
    dct = dict(max_power=maxx["power"], min_power=minn["power"],
               avg_power=avg)
    return dct


if __name__ == "__main__":
    artifacts = [
            {
                'name': 'Shadow Blade',
                'power': 93,
                'type': 'armor'
                },
            {
                'name': 'Lightning Rod',
                'power': 108,
                'type': 'armor'
                },
            {
                'name': 'Water Chalice',
                'power': 118,
                'type': 'focus'
                },
            {
                'name': 'Water Chalice',
                'power': 103,
                'type': 'weapon'
                }
            ]
    mages = [
            {
                'name': 'Zara',
                'power': 55,
                'element':
                'earth'
                },
            {
                'name': 'Morgan',
                'power': 69,
                'element': 'lightning'
                },
            {
                'name': 'Casey',
                'power': 56,
                'element': 'ice'
                },
            {
                'name': 'Sage',
                'power': 66,
                'element': 'lightning'
                },
            {
                'name': 'Luna',
                'power': 92,
                'element': 'lightning'
                }
            ]
    spells = ['earthquake', 'freeze', 'fireball', 'tornado']

    print("\nTesting artifact sorter...")
    s_test = artifact_sorter(artifacts)
    print(f"{s_test[0]['name']} ({s_test[0]['power']}) comes before "
          f"{s_test[1]['name']} ({s_test[1]['power']})")

    print("\nTesting power filter...")
    f_test = power_filter(mages, 67)
    print("Filtering powers that are less than (67): ", end="")
    for n in f_test:
        print(f"{n['name']}->{n['power']} ", end="")

    print("\n\nTesting spell transformer...")
    t_test = spell_transformer(spells)
    for m in t_test:
        print(f"{m} ", end="")

    print("\n\ngetting mage stats...")
    stats = mage_stats(mages)
    print(stats)
