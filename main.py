import model

import os
import re

def main():
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    print("Your current job application options are: " + str(job_options))
    print("Please choose which job application you would like to work on: ")

    user_input = input("You: ")

    while not user_input in job_options:

        print("Please try again, pick one of these values:" + str(job_options))
        user_input = input("You: ")

    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]

    job = user_input

    print("Awesome, we are working on your " + job + " application.")
    print("Here's the skills I have identified!")
    
    model.create_pick_out_skills_model()
    model.pick_out_skills(job)
    
    model.create_rank()

    print("Please pick a skill to rank")

    user_input = input("You: ")

    while not user_input in ranking_options:
        print("Please try again, pick one of these values: " + str(ranking_options))
        user_input = input("You: ")

    ranking = user_input
    print("Groovy, we will be ranking your " + ranking + ".")

    model.rank(ranking)

if __name__ == "__main__":
    main()
