#import sys 
#from rich import print 
#from time import sleep
#import time

#def printLyrics():
    #lines = [
        #("I wanna da-", 0.06), #1
       # ("I wanna dance in the lights", 0.05) , #2
        #("I wanna ro-", 0.07), #3
      #  ("I wanna rock your body", 0.08), #4
       # ("I wanna go-", 0.08), #5
      #  ("I wanna go for a ride", 0.068), #6
       # ("Hop in the muscic and", 0.07), #7
      #  ("Rock your body", 0.08), #8
       # ("Rock that body", 0.069), #9
        #("come on, come on", 0.035), #10
       # ("Rock that body", 0.05), #11
        
        
        
        
   # ]
   
import sys
import time

def printLyrics():
    lines = [
("I wanna da-", 0.06),
("I wanna dance in the lights", 0.05),
("I wanna ro-", 0.08),
("I wanna rock your body", 0.08),
("I wanna go-", 0.08),
("I wanna go for a ride", 0.068),
("Hop in the music and", 0.07),
("Rock your body", 0.08),
("Rock that body", 0.069),
("come on, come on", 0.035),
("Rock that body", 0.05),
("(Rock your body)", 0.03),
("Rock that body", 0.049),
("come on, come on", 0.035),
("Rock that body", 0.08),
]

for text, delay in lines:
    for ch in text:
        sys.stdout.write(ch)
sys.stdout.flush()
time.sleep(delay)
sys.stdout.write("\n")
sys.stdout.flush()
time.sleep(0.6)

if __name__ == "__main__":
    printLyrics()
    
    
    