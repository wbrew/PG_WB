import pyautogui as pg
import time
import webbrowser

points = 0

#Question
answer = pg.prompt(
"""
Which team do you like?

a)Thunder
b)Caveliers
c)Warriors
d)Knickerbockers
"""
    )


#give points

if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
    

#Question
answer = pg.prompt(
"""
Who is your favorite NBA player?

a)Russel Westbrook
b)Lebron James
c)Steph Curry
d)Kristaps Porzingis
"""
    )


#give points

if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


#Question
answer = pg.prompt(
"""
Who is the best NBA player of all time

a)Lebron James
b)Micheal Jordan 
c)Kobe Bryant
d)Steph Curry
"""
    )


#give points

if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


    
#Question
answer = pg.prompt(
"""
Who is your least favorite player?

a)Kristaps Porzingis
b)Steph Curry
c)Lebron James
d)Russel Westbrook
"""
    )


#give points

if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# END OF SURVEY

pg.alert("You are...")

#Smart
if points <8:
    pg.alert("Smart")
#You're OK
elif points >= 8 and points < 12:
    pg.alert("You're OK")
#Dumb
elif points >= 12 and points < 16:
    pg.alert("Dumb")
#Complete idiot
elif points >= 16:
    pg.alert("Complete Idiot")




