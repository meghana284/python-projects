score = 0

print("Welcome to the Python Quiz Game")
print()

q1 = input("1. What does CPU stand for? ")
if q1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

q2 = input("2. What does RAM stand for? ")
if q2.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

q3 = input("3. What does GPU stand for? ")
if q3.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()
print("Your score is:", score)
