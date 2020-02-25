import random

gestures = ["rock", "paper", "scissors"]
n_round = 0
n_rounds = 3
rounds_to_win = n_rounds + 1 / 2
cpu_score = 0
player_score = 0


def choice_cpu_gesture():
    return random.choice(gestures)


def choice_player_gesture():
    choice = ""
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input("choose between 'rock', 'paper' or 'scissors'")
    return choice


def who_win():
    if cpu_score == player_score:
        return 0
    elif cpu_score > player_score:
        return 1
    else:
        return 2


def current_round(cpu_score, player_score):
    win = 0
    choice_cpu = choice_cpu_gesture()
    choice_player = choice_player_gesture()
    if choice_cpu == "rock" and choice_player == "scissors" \
            or choice_cpu == "paper" and choice_player == "rock" \
            or choice_cpu == "scissors" and choice_player == "paper":
        cpu_score += 1
        win = 1
    if choice_player == "rock" and choice_cpu == "scissors" \
            or choice_player == "paper" and choice_cpu == "rock" \
            or choice_player == "scissors" and choice_cpu == "paper":
        player_score += 1
        win = 2
    print("CPU ", choice_cpu)
    print("Player ", choice_player)
    if win == 1:
        print("round winner CPU")
    if win == 2:
        print("round winner Player")

    return cpu_score, player_score


while cpu_score < rounds_to_win and player_score < rounds_to_win and n_round < n_rounds:
    cpu_score, player_score = current_round(cpu_score, player_score)
    n_round += 1

won = who_win()
if won == 0:
    print("Draw")
elif won == 1:
    print("CPU won")
elif won == 2:
    print("Player won")
