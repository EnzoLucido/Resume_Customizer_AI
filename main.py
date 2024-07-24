import model

import pick_out_skills
import ranking

import os
import re

def main():
    #models should be created only once for all
    model.create_all_models()

    #additionally, job_options and ranking_options should be read only once
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]
    
    pick_out_skills.pick_out(job_options)    
    ranking.rank(ranking_options)
    print("Please pick a skill to rank")
    #ranking_section()

if __name__ == "__main__":
    main()
