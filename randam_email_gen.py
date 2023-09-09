import random

def genrate_email():
    # names list will be populated from data.txt file
    names_list = []
    # email providers
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance","company", "corporation", "community"]
    no_list = [0,1,2,3,4,5,6,7,8,9]
    email = ""
    with open("data.txt","r",encoding="UTF-16") as file:
        for line in file:
            names_list.append(line.removesuffix("\n"))
        
    for i in random.choices(names_list,k=2):
        email = f"{email}{i}"
    for i in random.choices(no_list,k=4):
        email = f"{email}{i}"
    
    return f"{email}@{random.choice(domains)}.com"


print(genrate_email())

    
    