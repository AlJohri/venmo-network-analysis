# Venmo Network Analysis

## Usage

### Download Venmo Contacts

First [set up Chrome DevTools snippets](#set-up-chrome-devtools-snippets) with the `console.save` function.

```
console.save(venmo.contacts, "contacts.json");
```

### Download Transaction Data for All Contacts

First [set up python](#set-up-python).

Then, log into Venmo and open the Chrome DevTools. Observe the headers of any outgoing XHR request. Copy the entire string of the `Cookie: ` header and paste it into the `.secret` file. This must be done for every "session".

```
source .secret
python download_transactions.py
```

## Setup

### Set up Chrome DevTools Snippets

The following steps will allow you to use the `console.save` function within the Chrome DevTools console.

1. View -> Developer -> Developer Tools
2. Click the Sources Tab.
3. Within the left pane of this window, click the Snippets tab.
4. Right click in the blank area of the left pane and click New.
5. Name the file `console-save.js`.
6. Paste the contents of [`snippets/console-save.js`](./snippets/console-save.js) from this repository.
7. Right click on the script and click Run.

### Set up Python

Use Python 3.5.1.

```
pip install -r requirements.txt
cp .secret.example .secret
# fill in the CELLPHONE and PASSWORD data for Venmo login
```

