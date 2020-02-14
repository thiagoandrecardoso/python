import random

gestures = ["rock", "paper", "scissors"]

n_round = 0
n_rounds = 3
rounds_to_win = n_rounds + 1 / 2

cpu_score = 0
player_score = 0


def choiceCPUGesture():
    return random.choice(gestures)


def choicePlayerGesture():
    choice = ""
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input("choose between 'rock', 'paper' or 'scissors'")

    return choice


def whoWin():
    if cpu_score == player_score:
        return 0
    elif cpu_score > player_score:
        return 1
    else:
        return 2


def currentRound(cpu_score, player_score):
    win = 0
    choiceCPU = choiceCPUGesture()
    choicePlayer = choicePlayerGesture()
    if choiceCPU == "rock" and choicePlayer == "scissors" \
            or choiceCPU == "paper" and choicePlayer == "rock" \
            or choiceCPU == "scissors" and choicePlayer == "paper":
        cpu_score += 1
        win = 1
    if choicePlayer == "rock" and choiceCPU == "scissors" \
            or choicePlayer == "paper" and choiceCPU == "rock" \
            or choicePlayer == "scissors" and choiceCPU == "paper":
        player_score += 1
        win = 2
    print("CPU ", choiceCPU)
    print("Player ", choicePlayer)
    if win == 1:
        print("round winner CPU")
    if win == 2:
        print("round winner Player")

    return cpu_score, player_score


while cpu_score < rounds_to_win and player_score < rounds_to_win and n_round < n_rounds:
    cpu_score, player_score = currentRound(cpu_score, player_score)
    n_round += 1

won = whoWin()
if won == 0:
    print("Draw")
elif won == 1:
    print("CPU won")
elif won == 2:
    print("Player won")
