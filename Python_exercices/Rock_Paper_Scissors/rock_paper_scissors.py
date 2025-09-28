# Generate an algorithm that simulates a Rock, Paper, Scissors game using recursion
# Only 3 times

import random

# Mapping which choice beats which
your_win_case = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

def game(election, machine_election, table=None, index=0, history=None):
    if table is None:
        table = {"you": 0, "machine": 0}
    if history is None:
        history = []

    # Base case: if someone reached 2 wins or no more moves
    if table["you"] == 2 or table["machine"] == 2 or index >= len(election):
        return table, history

    # Store choices this round
    history.append((election[index], machine_election[index]))

    if election[index] == machine_election[index]:
        return game(election, machine_election, table, index + 1, history)
    if your_win_case[election[index]] == machine_election[index]:
        table["you"] += 1
    else:
        table["machine"] += 1
    return game(election, machine_election, table, index + 1, history)


plays = ['rock', 'scissors', 'paper']

# elections
election = ['rock', "scissors", 'rock']
machine_election = [random.choice(plays) for _ in range(3)]

result, history = game(election, machine_election, None, 0, None)
print("Your choices:     ", election)
print("Machine choices:  ", machine_election)
print("Round history (You, Machine):")
for i, (y, m) in enumerate(history, 1):
    print(f"Round {i}: You -> {y} | Machine -> {m}")

print("Final score:      ", result)

if result["you"] > result["machine"]:
    print("You won the best 2 out of 3!")
elif result["you"] < result["machine"]:
    print("Machine won the best 2 out of 3!")
else:
    print("It's a tie!")
