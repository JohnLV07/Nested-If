#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them

place = input("Choose a place (forest or cave)? :")

if place == "forest":
    action = input("climb a tree or cross a river? :")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    elif place == 'cave':
     print("You find a hidden treasure!")
     
#Task 2: Setting the Scene: 
#Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

elif place == "cave":
      action =input("Do you want to light a torch? (yes/no) :")
      if action == 'yes':
            print("Here's some light for your path")
      elif action == 'no':
            print("proced in the dark carefully")

#Task 3: Default Path:
# If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?
else:
    pass #This should avoid the other 2 options and send me to my default options
    print("You seem indecisive head home for now")
    
