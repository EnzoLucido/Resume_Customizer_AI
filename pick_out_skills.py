import model

def pick_out(job_options):
    
    print("Your current job application options are: " + str(job_options) + "\n")
    print("Please choose which job application you would like to work on: \n")

    job = input("You: ")

    while not job in job_options:

        print("Please try again, pick one of these values:" + str(job_options))
        job = input("You: ")

    print("Awesome, we are working on your " + job + " application.")
    print("Please wait while I identify skills")

    model.pick_out_skills(job)

    next_step = input("You: ")
    while not next_step in ["modify", "continue"]:
        print("Please reply modify, continue or quit\n")
        next_step = input("You: ")
        if next_step == "modify":
            modify.modify()

    return job



