#$python ex14.py farnaz
from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, i'm the {script} script.")
print("i'd like to ask u a few questions.")

print(f"do u like me {user_name}?")
like = input(prompt)

print(f"where do u live {user_name}?")
live = input(prompt)

print(f"""so u said u love {user_name}.
you said u living in {live}.""")