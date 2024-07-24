import model

import os
import re

def main():
    #models should be created only once for all
    model.create_all_models()

    #additionally, job_options and ranking_options should be read only once
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]
    
    print("Your current job application options are: " + str(job_options) + "\n")
    print("Please choose which job application you would like to work on: \n")

   

    user_input = input("You: ")

    while not user_input in job_options:

        print("Please try again, pick one of these values:" + str(job_options))
        user_input = input("You: ")

    job = user_input

    print("Awesome, we are working on your " + job + " application.")
    print("Please wait while I identify skills")
    
    model.pick_out_skills(job)

    print("Please pick a skill to rank")
    ranking_section()

if __name__ == "__main__":
    main()
