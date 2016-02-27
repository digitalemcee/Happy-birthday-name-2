name = raw_input("What's your name? \nType name: ")
guess = raw_input("Is today your birthday? \nyes or no: ").lower()
if guess == "yes" or guess == "y": 
    print "Happy Birthday,",name + "!"
elif guess == "no" or guess == "n":
    print "Have a nice day,",name + "!"
else:
  print "You didn't type yes or no! Be fair."
raw_input("\nSee you next time.")