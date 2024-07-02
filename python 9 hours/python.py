print("welcome to my computer quiz")
playing =input('do you wannt to paly?')
if playing.lower() != 'yes':
    quit()
    print("Okay! Let's play:")
    print("Write all answer must small letter: ")
score = 0
answer = input("what does cpu stand for")
if answer.lower() == "central processing unit":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does ROM stand for")
if answer.lower() == "read only memory":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does pc stand for")
if answer.lower() == "personal computer":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does pdF stand for")
if answer.lower() == "portable document format":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does ac stand for")
if answer.lower() == "alternate current":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does dc for")
if answer.lower() == "dirrect current":
    print("correct!")
    score +=1
else: 
    print("incorrect")

answer = input("what does ram stand for")
if answer.lower() == "random access memory":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does AI stand for")
if answer.lower() == "artificial intelligence":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does BIOS stand for")
if answer.lower() == "basic input output system":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does HDD stand for")
if answer.lower() == "hard disk drive":
    print("correct!")
    score +=1
else: 
    print("incorrect")
answer = input("what does OS stand for")
if answer.lower() == "operating system":
    print("correct!")
    score +=1
else: 
    print("incorrect")
print("Congrats! you try to solve quiz!")
print('You got  ' +str(score)+ " question correct")
print("You got " +str((score/11)*100)+"%.")