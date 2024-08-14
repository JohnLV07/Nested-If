#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" 
if attendees >= 100:
    print(venue)
elif attendees <= 100:
    print("conference room")

#Task 2: Venue Selection:
#Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.
action = input("Do you require assistance (audio system or projector)? ")
if action == 'audio system' and attendees > 100:
    print('We will provide a large hall with audio system')
elif action == 'projector' and attendees < 100:
    print("We will have the conference room ready with the projector")
else:
    print("Your request will be accommodated based on availability.")

#Task 3 Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers"

catering = input("What food would you like? (vegetarian/gourmet)? ")
if catering == 'vegetarian':
    catering_choice = input("Would you like Veggie Delight Caterers? (yes/no) ")
    if catering_choice == 'yes':
        print("Very well, enjoy your veggies!")
    elif catering_choice == 'no':
        print("Some rice and beans then!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
else:
    print("Gourmet meals are on the way!")
    