name = raw_input("Good afternoon. What's your name? \nType name: ")
guess = raw_input("I have a question - Is today your birthday? \nyes or no: ").lower()
if guess == "yes" or guess == "y": 
    print "Happy Birthday to you,",name + "!"
elif guess == "no" or guess == "n":
    print "Have a nice day anyway,",name + "!"
else:
  print "You didn't type yes or no! Don't be evil!"
raw_input("\nThanks for playing. See you next time.")
