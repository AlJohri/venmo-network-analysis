import os, sys, json, itertools
from pprint import pprint as pp

with open("contacts.json") as f:
    contacts = json.load(f)
    
contacts_dict = {contact['user_id']:contact for contact in contacts}

users = []

folder = "data"

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        user_id = int(filename.replace(".json", ""))
        with open(folder + "/" + filename) as f:
            data = json.load(f)
            user = {
                "user_id": user_id,
                "transactions": data
            }
            users.append(user)

users = [user for user in users if len(user['transactions']) != 0]

f = open("edges.csv", "w")
f.write("source,target\n")

for user in users:
    user_id = user['user_id']
    contact = contacts_dict[user_id]

    print(contact['id'], contact['username'], contact['full_name'])

    for payment in user['transactions']:

        # not sure why this is a list
        assert(len(payment['transactions']) == 1)

        transaction = payment['transactions'][0]

        if type(transaction['target']) == str or transaction['target'] is None or \
            transaction['target'].get('id') is None:
            print("-----------------")
            pp(payment)
            print("Ignoring Transaction")
            print("-----------------")
            continue

        actor = payment['actor']
        target = payment['transactions'][0]['target']

        print(
            "From: ", actor['id'], actor['name'], "\t\t",
            "To: ", target['id'], target['name']
        )

        f.write("{actor_id},{target_id}\n".format(actor_id=actor['id'], target_id=target['id']))

    print("\n")
        
f.close()