import os
import re

def main():
    
    ranking_options = [option[:-4] for option in os.listdir('user_info/ranking')]
    
    print(ranking_options)

if __name__ == "__main__":
    main()
