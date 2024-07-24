import model
import modify

'''
    Handling Section of ranking
    Relies on modify.py for more complex options
'''

def ranking_all(ranking_options):
    for option in ranking_options:
        if not option == "all":
            model.rank(option)
    print("\n")


def ranking_section(ranking_options):
    ranking_options.append("all")

    print("Please pick a skill to rank")

    user_input = input("You: ")

    while not user_input in ranking_options:
        print("Please try again, pick one of these values: " + str(ranking_options) + "\n")
        user_input = input("You: ")

    ranking = user_input
    print("Groovy, we will be ranking your " + ranking + ".")

    if ranking == "all":
        ranking_all(ranking_options)


    model.rank(ranking)
    print("\n")
    print("Do you want to modify these skills, continue with another section or quit? Reply modify, continue or quit\n")

    user_input = input("You: ")
    while not user_input in ["modify", "continue", "quit"]:
        print("Please reply modify, continue or quit\n")
        user_input = input("You: ")
    if user_input == "modify":
        modify()
    elif user_input == "yes":
        ranking_section()

