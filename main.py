print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("How old are you? "))
	if age < 12:
		bill = 5
		print("Child tickets are $5")
	elif age <= 18:
		bill = 7
		print("Youth tickets are $7")
	elif age >= 45 or age <= 55:
		bill = 0
		print("Your ticket is $0")
	else:
		bill = 12
		print("Adult tickets are $12")

	wants_photo = input("Would you like a photo taken? (Y/N)")
	if wants_photo == "Y" or wants_photo == "y":
		bill += 3

	print(f"Your total ticket price is ${bill}")
else:
	print("Sorry, you have to be taller before you can ride.")
  