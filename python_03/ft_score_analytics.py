import sys

print("=== Player Score Analytics ===")
scores = []
if (len(sys.argv) < 2):
    print("No scores provided. Usage: python3", end='')
    print(" ft_score_analytics.py <score1> <score2> ...")
else:
    i = 1
    while (i < len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
            pass
        i += 1
if (len(scores) < 1):
    print("No scores provided. Usage: python3", end='')
    print(" ft_score_analytics.py <score1> <score2> ...")
else:
    print(f"{scores}")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores) - 1}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
