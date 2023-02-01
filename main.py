print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("How old are you? "))
	if age <= 18:
		print("Your ticket is $7")
	else:
		print("Your ticket is $12")
else:
	print("Sorry, you have to be taller before you can ride.")
  