#Tip Caculator!


bill = float(input("What was the total bill?\n $")) #ask for total bill

tip = float(input("What percentage Tip would you like to give?\n %")) # ask percentage to tip

group = int(input("How many people to split the bill?\n ")) # ask how many people are splitting 

print(f"Each one of you should pay: ${'{:.2f}'.format(bill / group + (bill * ((tip / 100) / group)))}") #all the maths 