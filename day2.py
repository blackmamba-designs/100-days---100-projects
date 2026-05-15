print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

if tip==10:
    total_tip = (bill/people) * 10/100
    print("The tip per person is: ", round(total_tip,2))
elif tip==12:
    total_tip = (bill/people) * 12/100
    print("The tip per person is: ", round(total_tip,2))
elif tip==15:
    total_tip = (bill/people) * 15/100
    print("The tip per person is: ", round(total_tip,2))
else:
    print("Please enter a valid tip!!")