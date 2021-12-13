from dfa import DFA

states = input("Enter the states in DFA: ").split()
start_state = str(input("Enter the start state in DFA: "))
final_states = input("Enter the final states in DFA: ").split()
inputs = input("Enter the input symbols in DFA: ").split()
transitions = {}

print("Please enter the transitions in the format \
(State1 input State2) \n Enter * to stop")
while True:
  transition = input().split()
  if (transition == ['*']):
    break
  transitions[(transition[0], transition[1])] = transition[2]


dfa = DFA(states, start_state, transitions,final_states, inputs)
dfa.printDFA()

# minimize dfa
dfa.minimize()

# print minimized dfa
dfa.printDFA()