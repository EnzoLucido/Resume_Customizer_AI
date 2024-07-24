import ollama

'''
    Create ALL models
    Handles ALL ollama logic
'''

def read_instruction(instruction):
    with open('instructions/' + instruction + '.txt') as file:
        return file.read()

def read_job(job):
    with open('fill_me_out/job_info/' + job + '.txt') as file:
        return file.read()

def read_skill(skill):
    with open('fill_me_out/user_info/ranking/' + skill + '.txt') as file:
        return file.read()

def remember_skills(job):
    skills_path = "output/picked_out_skills/{}.txt".format(job)
    with open(skills_path) as file:
        return file.read()

def create_pick_out_skills_model():
    instruction = read_instruction("pick_out_skills")

    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    # Create the model using ollama
    ollama.create(model='pick_out_skills', modelfile=modelfile)


def create_rank_model(job):
    remembered_skills= remember_skills(job)
    instruction = read_instruction("rank").format(remembered_skills)
    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='rank', modelfile=modelfile)

def pick_out_skills(job, feedback=""):

    query = read_job(job)
    skills_path = "output/picked_out_skills/{}.txt".format(job) 
    stream = ollama.chat(
            model='pick_out_skills',
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )
    
    # Open a file in write mode
    with open(skills_path, "w") as output_file:
        # Initialize a variable to store the full string
        full_content = ""

        # Iterate through the stream
        for chunk in stream:
            # Extract the message content
            content = chunk['message']['content']

            # Print to console
            print(content, end='', flush=True)

            # Append the content to the full_content string
            full_content += content

        # Write the full content to the file
        output_file.write(full_content)


def rank(skill, feedback=""):
    query = read_skill(skill)

    stream = ollama.chat(
            model='rank',
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
