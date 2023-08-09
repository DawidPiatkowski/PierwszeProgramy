import requests
import json

"""
{
  1 : 11
  2 : 8
  3 : 15

  10: 
}

"""

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser

def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ] 

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []    
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o id: ", usersWithTopCompletedTasks)
             

