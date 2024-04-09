states = []
alphabets = []
start_state = ""
accept_states = []
transition = {}

input_string = ""

print("Enter the automaton states separated by space: ", end="")
states = input().split()

print("Enter the automaton alphabets separated by space: ", end="")
alphabets = input().split()

print("Enter the start state of the automaton: ", end="")
start_state = input()

print("Enter the final states of the automaton separated by space: ", end="")
accept_states = input().split()

print("Enter the next states for the following (enter . for dead/null state)")
for state in states:
    for alpha in alphabets:
        print(f"\t  {alpha}")
        print(f"{state}\t---->\t", end="")
        dest = input()

        if dest == ".":
            transition[(state, alpha)] = None
        else:
            transition[(state, alpha)] = dest

print("Enter the input string to run the automaton: ", end="")
input_string = input()

current_state = start_state

for char in input_string:

    current_state = transition[(current_state, char)]

    if current_state is None:
        print("Rejected")
        break
else:

    if (current_state in accept_states):
        print("Accepted")
    else:
        print("Rejected")
