name=input("Hello! I am AI Bot.What's your name?:")
print(f"Nice to meet you, {name}!")
mood=input("how are you feeling today? (good/bad):")
if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad":
    print("I'm sorry to hear that. Hope things get better soon")
else:
    print("I see. sometimes its hard to put feelings into words")
print(f"it was nice chatting with you {name}.Goodbye!")
