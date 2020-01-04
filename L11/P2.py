# wapp to generate a random motivational message
#from a list of message

msg = ["maine bohat struggle kiya hai","the best things in life are really","just do it","never give up","never sat never",
"not planning is planning to fail","change is constant"]

import random 
r = random.randrange(len(msg))
print(msg[r])