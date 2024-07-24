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


def rank(ranking_options):
    ranking_options.append("all")

    print("Please pick a skill to rank")

    skill = input("You: ")

    while not skill in ranking_options:
        print("Please try again, pick one of these values: " + str(ranking_options) + "\n")
        skill = input("You: ")

    print("Groovy, we will be ranking your " + skill + ".")

    if skill == "all":
        ranking_all(ranking_options)


    model.rank(skill)
    print("\n")
    print("Do you want to modify this ranking, continue with another section or quit? Reply modify, continue or quit\n")

    next_step = input("You: ")
    while not next_step in ["modify", "continue", "quit"]:
        print("Please reply modify, continue or quit\n")
        next_step = input("You: ")
    if next_step == "modify":
        modify.modify()
    elif next_step == "yes":
        ranking_section()


    return skill
