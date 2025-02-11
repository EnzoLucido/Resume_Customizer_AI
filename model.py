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

def create_pick_out_skills_model():
    instruction = read_instruction("pick_out_skills")

    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    # Create the model using ollama
    ollama.create(model='pick_out_skills', modelfile=modelfile)


def create_rank_model():
    instruction = read_instruction("rank")
    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='rank', modelfile=modelfile)

def create_all_models():
    create_pick_out_skills_model()
    create_rank_model()

def pick_out_skills(job, feedback=""):

    query = read_job(job)

    stream = ollama.chat(
            model='pick_out_skills',
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def rank(skill, feedback=""):
    query = read_skill(skill)

    stream = ollama.chat(
            model='rank',
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
