import os, sys, json, time, requests
from pprint import pprint as pp

os.makedirs("data", exist_ok=True)

USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"

CELLPHONE = os.getenv("CELLPHONE")
PASSWORD = os.getenv("PASSWORD")
COOKIES = os.getenv("COOKIES")

s = requests.Session()
s.headers = {"User-Agent": USER_AGENT, "Cookie": COOKIES}

current_time = int(time.time())

with open("contacts.json") as f:
    contacts = json.load(f)

for contact in contacts:

    contact_filename = "data/" + str(contact['user_id']) + ".json"

    if os.path.isfile(contact_filename):
        print("Already downloaded data for [%s] %s" % (contact['user_id'], contact['full_name']))
        continue

    transactions = []

    page = 1
    url = "https://venmo.com/api/v5/users/%s/feed?until=%s&limit=1000" % (contact['user_id'], current_time)

    while True:
        data = s.get(url).json()
        try:
            transactions += data['data']
        except KeyError:
            print("Tried Downloading data for page %d [%s] %s but ran into an error" % (page, contact['user_id'], contact['full_name']))
            print("This was the data returned from the API:")
            print(data)
            break
        
        if len(data['data']) == 0:
            print("Tried Downloading data for page %d [%s] %s but no transactions" % (page, contact['user_id'], contact['full_name']))
            break
        else:
            print("Downloaded page %d data for [%s] %s" % (page, contact['user_id'], contact['full_name']))

        page += 1
        url = data['paging']['next']

    with open(contact_filename, "w") as f:
        json.dump(transactions, f)

    print()
