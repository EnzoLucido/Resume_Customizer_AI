import model

import os
import re

def ranking_section():
    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]
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

def modify():


def ranking_all(ranking_options):
    for option in ranking_options:
        if not option == "all":
            model.rank(option)
    print("\n")

def main():
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    print("Your current job application options are: " + str(job_options) + "\n")
    print("Please choose which job application you would like to work on: \n")

    user_input = input("You: ")

    while not user_input in job_options:

        print("Please try again, pick one of these values:" + str(job_options))
        user_input = input("You: ")

    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]

    job = user_input

    print("Awesome, we are working on your " + job + " application.")
    print("Please wait while I identify skills")
    
    model.create_pick_out_skills_model()
    model.pick_out_skills(job)
    
    model.create_rank()

    print("Please pick a skill to rank")

    ranking_section()

if __name__ == "__main__":
    main()
