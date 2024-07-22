def instruction(instruction):
    with open('instructions/' + instruction + '.txt'):
        return file.read()

def job(job):
    with open('../fill_me_out/job_info/' + job + '.txt')
        return file.read()

def skill(skill):
    with open('../fill_me_out/user_info/ranking/' + skill + '.txt')
        return file.read()

def create_pick_out_skills_model():
    instruction = instruction(pick_out_skills)
    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='pick_out_skills', modelfile=modelfile)

def create_rank():
    instruction = instruction(rank)
    modelfile = f'''
    FROM llama3
    SYSTEM "{instruction}"
    '''
    ollama.create(model='rank', modelfile=modelfile)

def pick_out_skills(job, feedback=""):

    query = job(job) 

    stream = ollama.chat(
            model='pick_out_skills',
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def rank(rank, feedback=""):
    query = skill(skill)

    stream = ollama.chat(
            model='rank'
            messages=[{'role':'user', 'content': query}],
            stream=True,
        )

    for chunk in stream:
        print(chunk['message']['content': query], end='', flush=True)
