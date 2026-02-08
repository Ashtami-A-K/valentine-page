import time

messages = [
    "I'm sorry for not attending your call... sothe💔",
    "I really miss you...",
    "Will you be my Valentine? ❤️"
]

for msg in messages:
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(0.08)
    print("\n")
    time.sleep(1)
