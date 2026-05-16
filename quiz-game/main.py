print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

score = 0

answer = input("Which keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which data type stores True or False values in Python? ")
if answer.lower() == "bool":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which loop is used when the number of iterations is known? ")
if answer.lower() == "for":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which keyword is used to import modules in Python? ")
if answer.lower() == "import":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your score is : ", score)