print("Welcome To My Python Quiz Game \nInteresting Game to Play")
Player = input("Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :",name_player)

score = 0

answer = input('Q1-What is PEP stands for in Python? \nAns- ')
if answer.lower() == 'python enhancement proposal':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : python enhancement proposal ')

answer = input('Q2-What is GIL stands for in Python? \nAns- ')
if answer.lower() == 'global interpreter lock':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : global interpreter lock ') 

answer = input('Q3-What is PIP stands for in Python? \nAns-')
if answer.lower() == 'pip installer package':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : pip installer package ')

answer = input('Q4-What is IDLE stands for in Python? \nAns-')
if answer.lower() == 'integrated development and learning environment':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : integrated development and learning environment ')

answer = input('Q5-What is OOP stands for in Python? \nAns-')
if answer.lower() == 'object oriented programming':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : object oriented programming ')

answer = input('Q6-What is API stands for in Python? \nAns-')
if answer.lower() == 'application programming interface':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : application programming interface ')

answer = input('Q7-What is DBMS stands for in Python? \nAns-')
if answer.lower() == 'database management system':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : database management system ')

answer = input('Q8-What is JSON stands for in Python? \nAns-')
if answer.lower() == 'javascript object notation':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : javascript object notation')

answer = input('Q9-What is CSV stands for in Python? \nAns-')
if answer.lower() == 'comma-separated values':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : comma-seprated values') 

answer = input('Q10-What is LTS stands for in Python? \nAns')
if answer.lower() == 'long-term support':
    print("Correct")
    score += 1
else:
    print('Wrong, The correct answer is : long-term support') 


print("You got the " + str(score)+ " correct answers")
print("You got " + str((score/10) * 100) + "% marks")

if score == 10: print(" Excellent! You are a Tech Genius!")
elif score >= 5: print(" Good job, keep learning!") 
else: print(" Better luck next time!")

