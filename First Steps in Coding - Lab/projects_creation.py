HOURS_PER_PROJECT = 3

architect_name = input()
number_of_projects = int(input())

hours_for_all_projects = HOURS_PER_PROJECT * number_of_projects

print(f"The architect {architect_name} will need {hours_for_all_projects} hours to complete {number_of_projects} project/s.")
