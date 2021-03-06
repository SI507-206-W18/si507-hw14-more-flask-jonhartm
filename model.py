import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init(app):
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        next_id = len(entries) + 1
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %I:%M %p")
    entry = {"id": str(next_id), "author": name, "text": text, "timestamp": time_string}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    for entry in entries:
        if entry['id'] == id:
            entries.remove(entry)
    # renumber the entries and reset the next_id
    new_id = 0
    for entry in entries:
        entry['id'] = new_id
        new_id += 1
    next_id = new_id
    with open(GUESTBOOK_ENTRIES_FILE, 'w') as f:
        f.write(json.dumps(entries))

def edit_entry(id, new_text):
    for e in entries:
        if e['id'] == str(id):
            e['text'] = new_text
            e['timestamp'] = datetime.now().strftime("%b %d, %Y %I:%M %p")
    with open(GUESTBOOK_ENTRIES_FILE, 'w') as f:
        f.write(json.dumps(entries))
