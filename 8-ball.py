print ("Welcome!!  Ask Magic 8-Ball anything")

question = input("What would you like to ask? ")
import random
result = random.randrange(1,9)

if result == 1:
     print("Yes - definitely.")
elif result == 2:
     print("It is decidedly so.")
elif result == 3:
     print("Without a doubt.")
elif result == 4:
     print("Reply hazy, try again.")
elif result == 5:
     print("Ask again later.")
elif result == 6:
     print("Better not tell you now.")
elif result == 7:
     print("My sources say no.")
elif result == 8:
     print("Outlook not so good.")
else:
     print("Very doubtful.")