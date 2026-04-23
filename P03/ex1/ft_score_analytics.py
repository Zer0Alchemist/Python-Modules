import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    lenght = len(sys.argv) - 1

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            " <score1> <score2> ...")
    else:
        try:
            scores = [int(arg) for arg in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {lenght}")
            print(f"Total score: {sum(scores)}")
            print("Average score:", sum(scores) / lenght)
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print("Score range:", max(scores) - min(scores))
        except ValueError:
            print("oops, i typed 'banana' instead of '1000'")
