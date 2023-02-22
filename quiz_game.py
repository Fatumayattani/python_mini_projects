print("Welcome to my Quiz Game! ")

Playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("okay! Let's play :)")
score = 0

answer = input("What is software engineering? ")
if answer.lower () == "software engineering is the process of designing,developing,and maintaing software using a systematic and structured approach.":
    print ('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What are the main principles of software engineering? ")
if answer.lower() == "The main principles of software engineering include design,testing,documentation,and maintenance.":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are the different phases of the software development life cycle? ")
if answer.lower() == "The different phases of the software development life cycle include requirements analysis,design,implementation,testing,and maintenance":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Agile software development? ")
if answer.lower() == "Agile software development is a method of software development that emphasizes flexibility,collaboration,and customer satisfaction ":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is scrum in software development? ")
if answer.lower() == "Scrum is an agile framework for software development that emphasizes teamwork,accountability,and iterative progress.":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the difference between a software engineer and software developer? ")
if answer.lower() == "A software engineer typically has more experience and education in the field of software development and may be involved in allaspects of the software development process,while a software developer may focus on specific tasks such as coding or testing. ":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")

answer = input("What are some popular programming languages used in software developement? ")
if answer.lower() == "Some popular programming languages used in software development include java,C++,python,c#,and javascript.":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are some common tools used in software development? ")
if answer.lower() == "Common tools used in software development include text editors,version control systems,debugging tools,and integrated development environments IDES.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is software testing? ")
if answer.lower() == "software testing is the process of evaluating the functionality of a software application or system to ensure it meets the specified requirements and works as intended.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input ("What is software maintenance? ")
if answer.lower() == "Software maintenance is the process of changing, modifying, and updating software to keep up with customer needs. Software maintenance is done after the product has launched for several reasons including improving the software overall, correcting issues or bugs, to boost performance, and more.":
   print("Correct!")
   score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
