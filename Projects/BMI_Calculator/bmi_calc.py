#function to calculate the BMI on the height and weight inputs by user.

def bmi(height,mass):
	b_index = mass/(height**2)
	return b_index

height = float(input("Enter the height in meters:"))
mass = float(input("Enter the weight in kg:"))
b_index = bmi(height,mass)
print("Your BMI is:","{0.2f}".format(b_index))