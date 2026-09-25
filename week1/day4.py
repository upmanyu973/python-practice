# Strings: slicing, f-strings, and the string methods

profession = "Coorporate advocate"
print(profession[0])
print (profession[-1])
print(profession[0:10])
print(profession[:12])
print(profession[7:])
print(profession[::-1])

#profession = input("enter your profession here")
#print(f"i am {profession}")

years = 5.3
print(f"You have {years} years of experience")
print(f"Rounded: {years:.1f} years")   # format spec after a colon — .0f = 0 decimal places

raw = "  Upmanyu@Incedo  "

print(len(raw))                 # length — a FUNCTION, not a property
print(raw.strip())              # removes leading/trailing whitespace
print(raw.strip().upper())      # methods chain, same as JS
print(raw.strip().lower())
print(raw.strip().split("@"))   # splits into a list: ['Upmanyu', 'Incedo  '.strip()... ]
print("-".join(["2026", "09", "17"]))   # '2026-09-17'
print(raw.strip().startswith("Upmanyu"))
print(raw.strip().find("Incedo"))       # returns index, or -1 if not found