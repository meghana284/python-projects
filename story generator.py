import random

subjects = ["A boy", "A girl", "A dog", "A teacher", "A robot"]
actions = ["found", "lost", "saw", "created", "liked"]
places = ["in the park", "at school", "in a city", "on the moon", "in a forest"]

print("Random Story Generator")

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    print("\nStory:")
    print(subject, action, "something", place)

    choice = input("\nGenerate another story? (yes/no): ")
    if choice.lower() != "yes":
        print("Goodbye!")
        break
