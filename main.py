import os
import re

def main():
    job_options = [option[:-4] for option in os.listdir('fill_me_out/job_info') if option.endswith('.txt')]
    print(job_options)

    ranking_options = [option[:-4] for option in os.listdir('fill_me_out/user_info/ranking') if option.endswith('.txt')]

    print(ranking_options)

if __name__ == "__main__":
    main()
