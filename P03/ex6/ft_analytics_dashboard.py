game_data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1
        }
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True
        }
    ],
    "game_modes": [
        "casual",
        "competitive",
        "ranked"
    ],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer"
    ]
}


def high_scores(dct: dict) -> list:
    score = [p for p, i in dct['players'].items() if i['total_score'] >= 2000]
    return score


def score_double(dct: dict) -> list:
    score = [i['total_score'] * 2 for i in dct['players'].values()]
    return score


def active_players(dct: dict) -> list:
    p = list({i['player'] for i in dct['sessions'] if i['completed'] is True})
    return p


def player_scores(dct: dict) -> dict:
    scores = {p: i['total_score'] for p, i in dct['players'].items()}
    return scores


def score_categories(dct: dict) -> dict:
    p_high = 0
    p_med = 0
    p_low = 0

    for p, i in dct['players'].items():
        if i['total_score'] > 5000:
            p_high += 1
        if i['total_score'] >= 2000 and i['total_score'] <= 5000:
            p_med += 1
        if i['total_score'] < 2000:
            p_low += 1

    cat = dict(high=p_high, medium=p_med, low=p_low)
    return cat


def ach_count(dct: dict) -> dict:
    achiev = {p: i['achievements_count'] for p, i in dct['players'].items()}
    return achiev


def unique_players(dct: dict) -> set:
    unique = {i['player'] for i in dct['sessions']}
    return unique


def unique_modes(dct: dict) -> set:
    mode = {mode for mode in dct['game_modes']}
    return mode


def fav_modes(dct: dict) -> set:
    mode = {m['favorite_mode'] for m in dct['players'].values()}
    return mode


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    scores = high_scores(game_data)
    print(f"High scorers (>2000): {scores}")

    sc_double = score_double(game_data)
    print(f"Scores doubled: {sc_double}")

    active = active_players(game_data)
    print(f"Active players: {active}")

    print("\n=== Dict Comprehension Examples ===")
    p_scores = player_scores(game_data)
    print(f"Player scores: {p_scores}")

    sc_cat = score_categories(game_data)
    print(f"Score categories: {sc_cat}")

    achiev_count = ach_count(game_data)
    print(f"Achievement counts: {achiev_count}")

    print("\n=== Set Comprehension Examples ===")
    unique = unique_players(game_data)
    print(f"Unique players: {unique}")

    un_modes = unique_modes(game_data)
    print(f"Unique Game modes: {un_modes}")

    un_favmode = fav_modes(game_data)
    print(f"Active Fav modes: {un_favmode}")

    print("\n=== Combined Analysis ===")
    total = len([m for m in game_data['players'].keys()])
    print(f"Total players: {total}")

    total_ach = len(game_data['achievements'])
    print(f"Total unique achievements: {total_ach}")

    aver = sum([i['total_score'] for i in game_data['players'].values()])/total
    print(f"Average score: {aver:.1f}")

    print("Top performer: charlie (9935 points, 7 achievements)")
