## This program simulates a simplified game of Yahtzee where a player
# plays against the computer.
# @author Karima
# Allow your program to use the randint function
import random
# Create and initialize pre-loop "constants"
YAHTZEE_POINTS = 50
TWO_OF_KIND_POINTS = 25
NUMBER_OF_DICES = 3
CONTINU = "Y"
TOTALP = 0
TOTALC = 0
# Create any other pre-loop variables you may need
# Continue to roll dice while the user enters an
# uppercase or lowercase Y.

def dice_role():
    dice = []
    for i in range(NUMBER_OF_DICES):
        dice.append(random.randint(1,6))
    return dice    

def dice_result(list):   
    occured = []
    count = 1
    for n in list:
        if n in occured:
            count +=1
        else:    
            occured.append(n)
    if count == 3:
        print("Yahtzee! (+"+str(YAHTZEE_POINTS)+")")
        result="Yahtzee"
    elif count == 2 :
        print("Two of a Kind! (+"+str(TWO_OF_KIND_POINTS)+")")
        result="2ofK"
    else:
        print("Chance! (+" + str(sum(list)) +")",)
        result="chance"
    return result 

def roll_points(list,result_roll,total):   
    if result_roll == "Yahtzee":
        total +=YAHTZEE_POINTS
    elif result_roll == "2ofK" :
        total +=TWO_OF_KIND_POINTS
    else:
        total += sum(list)
    return total    

def Print_report(total1,total2):
    print("\n=============================")
    print("Player total points: ", total1)
    print("Computer total points: ", total2)
    print("=============================\n")

while ((CONTINU == "Y") or (CONTINU == "y")):
# For the player, roll the three dice and display the dice values.
# You will need to remember each die value.
    # If the values rolled were all the same, display "Yahtzee!" and
    # and the number of points for a yahtzee are earned for the player
    # else if two values rolled were the same, display "Two of a Kind!" and
    # the number of points for two of a kind are earned for the player
    # else display chance and the sum of all three dice are earned for
    # the player
    # If you haven't already done so, tack the points earned onto
    # a running total for the player
    
    # For the computer, roll the three dice and display the dice values.
    # You will need to remember each die value.
    # If the values rolled were all the same, display "Yahtzee!" and
    # and the number of points for a yahtzee are earned for the computer
    # else if two values rolled were the same, display "Two of a Kind!" and
    # the number of points for two of a kind are earned for the computer
    # else display chance and the sum of all three dice are earned for
    # the computer
    # If you haven't already done so, tack the points earned onto
    # a running total for the computer
    # Show the current totals
    # Prompt whether to roll again        
      
    
    player =  dice_role()
    print("Player Rolls: " + str(player)[1:-1])
    presult=dice_result(player)
    TOTALP=roll_points(player,presult,TOTALP)
    
    
    computer=dice_role()
    print("Computer Rolls: " + str(computer)[1:-1])
    cresult=dice_result(computer)
    TOTALC=roll_points(computer,cresult,TOTALC)
    
    
    Print_report(TOTALP,TOTALC)
      
      
    CONTINU = input('Roll again (Y or N)? ')  