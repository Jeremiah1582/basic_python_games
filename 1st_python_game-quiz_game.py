print("welcome to my Computer quiz yo !!")

score=0
number_of_questions=5

playing = input("do you want to play?: ")
print("you said: ",playing)

if playing.lower() != "yes":
    print("you quit the game")
    quit()

print("ok, lets play")
# 1
answer = input("what does CPU stand for?: " )
if answer.lower() == "central processing unit":
    score += 1 #score= score+1 ,
    print("correct !")
else: 
    print("Incorrect !")
    # 2
answer = input("What does GPU stand for?: " )
if answer.lower() == "graphics processing unit":
    score += 1 #score= score+1 ,
    print("correct !")
    
else: 
    print("Incorrect !")
    # 3
answer = input("What does RAM stand for?: " )
if answer.lower() == "random access memory":
    score += 1 #score= score+1 ,
    print("correct !")
    
else: 
    print("Incorrect !")
    # 4
answer = input("what does PSU stand for?: " )
if answer.lower() == "power supply":
    score += 1 #score= score+1 ,
    print("correct !")
    
else: 
    print("Incorrect !")
    # 5
answer = input("What does AWS stand for?: " )
if answer.lower() == "amazon web services":
    score += 1 #score= score+1 ,
    print("correct !")
    
else: 
    print("Incorrect !")
    

print("you got a total of: "+ str(score)+ " correct answers" )

print("you scored "+str(score / 5 *100) + "%")