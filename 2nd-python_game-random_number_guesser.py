import random 


# .randrange
r= random.randrange(-1,11) #this will generate a random number from -1 to 10 (it wont generate the number 11)
print(r)

# .randint
num= random.randint(0,11) #this will generate a random number from 0 to 11 (it WILL generate the number 11)
print(num)
#Quit Vs Break
# quit will stop the code there and then
#break will stop the loop but allow the code to continue

# -------------------------------------------------
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range =int(top_of_range)
    if top_of_range <= 0 :
        print("please enter number greater than 0")
        quit() 
    if top_of_range >20: 
        print("top of range too high, keep number less than 20")
        quit()
else: 
    print("type a number next time")
    quit()

guesses=0
computer_number= random.randint(0,top_of_range)

while True: #its always true until a break or quit()
    guesses+=1
    user_guess = input("guess a number between "+ str(0)+ " and " + str(top_of_range)+": ") 
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else: 
        print("please add a number next time")
        continue #this restarts the while loop 
    if user_guess != computer_number:
        
        print("incorrect!! guess again")
        if user_guess > computer_number:
            print("your guess was toooo high ")
            continue
        if user_guess < computer_number:
            print("your guess was too low")
            continue
    else:
        print("you got it"+ str(user_guess)+ " is the correct answer" )
    
    print("you got it in", guesses, "guesses")

    reset= input("would you like to play again?: ")

    if reset.lower() != "yes":
        quit()
        # break # this will stop the while loop 
    else:
        top_of_range = input("Type a number: ")
        if top_of_range.isdigit():
            top_of_range =int(top_of_range)
            if top_of_range <= 0 :
                print("please enter number greater than 0")
                quit() 
            if top_of_range >20: 
                print("top of range too high, keep number less than 20")
                quit()
        else: 
            print("type a number next time")
            quit()

        guesses=0
        computer_number= random.randint(0,top_of_range)
        continue

    

  
   

    






