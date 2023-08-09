import requests
import json

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
             
"""
#sposob 1
    
r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    print(usersWithTopCompletedTasks)
    if (user["id"] in usersWithTopCompletedTasks):
        print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user["name"])

#sposob 2
for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user[0]["name"])
"""

#sposob 3

def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="
    
    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
    
    return conj_param
    
#conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")
conj_param = change_list_into_conj_of_param([2,7,4])
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_param)   

users = r.json()
for user in users:
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user["name"])
