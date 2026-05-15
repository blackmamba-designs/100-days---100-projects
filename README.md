Hey guys if you are starting to learn about python and want to do simple projects at start come join me in this journey. 
I will be updating notes here for each day I complete. 

Day 1 - 
    1. print() function helps you give the output you want the computer to show on the screen 
    2. "" these represent that the computer understands the value in these quotes is not a code but the output we want. 
    3. Concatenate helps in adding 2 or more strings together. Usually denoted by the ' + ' sign. 
    4. '\n' shifts the string to the next line. 
          eg - print(" What is your name? \n")
          result - What is your name?
                   Blackmamba designs
          --- as you can see the result of name is below the question because of '\n'
    5. '#' is the sign used to add a comment. It helps the PC in understanding that the line with # is not to be executed. 
    6. len() finds the lenght of the value inside. 
          eg - print(len(12345))
          result - 5 
          # 5 is the length if the value in len() function
    7. Day 1 project - Band Name Calculater : code 
         print("Welcome to the Band Name Calculator!!")
         city = input("What city do you live in?\n")
         pet = input("What is your pet's name?\n")
         print("Your Band name is: " + city + " " + pet)



Day 2 - 
    1. Data types - String ( str ), Integer ( int ), Float ( float ), Boolean ( bool ) 
    2. Subscripting is the way to seperate or distingusih individual elements in the value
           eg - print( " Hello " [0])
           result - H 
           # while sunscripting remember that the counting always starts from 0 and to get the end individual just use negative integers starting from -1. 
    3. To change one type form to another - 
           eg - print( int(3.6678) ) 
           result - 3
           # the int changed the float type that is decimal to a whole number. 
    4. Day 2 project - Tip Calculator: Code 
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
