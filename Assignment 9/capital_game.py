import random

QUIT = "0"

state_name_capital = {
     "California": "Sacramento",
    "Texas": "Austin",
    "New York": "Albany",
    "Florida": "Tallahassee",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Georgia": "Atlanta",
    "North Carolina": "Raleigh",
    "Michigan": "Lansing",
    "Washington": "Olympia",
    "Arizona": "Phoenix",
    "Massachusetts": "Boston",
    "Virginia": "Richmond",
    "New Jersey": "Trenton",
    "Colorado": "Denver",
    "Tennessee": "Nashville",
    "Maryland": "Annapolis",
    "Missouri": "Jefferson City",
    "Wisconsin": "Madison"
}


def main():
    correct = 0
    wrong = 0
    name_list = list(state_name_capital.keys())  # first make to list, because random cannot (dict)
    while True:
        state = random.choice(name_list)
        correct_answer_1 = state_name_capital.get(state)
        answer = input(f"What is the capital of {state}? (or enter {QUIT} to quit): ")
        if answer.strip() == QUIT:
            break
        else:
            answer = answer.strip()
            user_answer = answer.lower()
            correct_answer_1 = correct_answer_1.strip()
            correct_answer_2 = correct_answer_1.lower()
            if user_answer == correct_answer_2:
                correct += 1
                print("That is correct.")
            else:
                wrong += 1
                print("That is incorrect.")
            
    print(f"You had {correct} correct responses and {wrong} incorrect responses.")
            

if __name__=="__main__":
    main()
