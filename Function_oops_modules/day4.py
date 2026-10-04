# File I/O: reading/writing text & JSON; context managers (with)
import json
with open("person.json", "w") as f:
    details = {"name":"Parker", "age" :54, "work": "Plumber"}
    json.dump(details,f)

with open("person.json", "r") as f:
    print(json.load(f))