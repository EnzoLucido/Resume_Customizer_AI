import model

import pick_out_skills
import ranking

import os
import re

def main():

    #job_options and ranking_options should be read only once
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]
    
    model.create_pick_out_skills_model()
    job = pick_out_skills.pick_out(job_options)    
    
    model.create_rank_model(job)
    ranking.rank(ranking_options)
    print("Please pick a skill to rank")
    #ranking_section()

if __name__ == "__main__":
    main()
