print("BMI Calculator")
while True:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print("BMI Category:", category)
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using BMI Calculator")
        break
