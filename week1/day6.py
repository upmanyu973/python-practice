# Dicts & sets in depth. Build a CLI word-frequency counter script.

profile = {"name": "Upmanyu", "role": "Frontend Dev", "years": 5.3}

print(profile.get("role"))
print(profile["years"])
print(profile.get("company", "Not Available"))

for key, value in profile.items():
    print(key, "=>" , value)

frontend = {"react", "redux", "typescript", "html"}
backend = {"python", "sql", "docker", "html"}

print(frontend | backend)   # union — everything in either
print(frontend & backend)   # intersection — in both ("html")
print(frontend - backend)   # difference — in frontend only