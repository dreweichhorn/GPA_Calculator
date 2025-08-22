import GPA_Calc_class as gc

grades = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

# Create an instance of the Calc class
calc = gc.calc(grades)

# Get the number of classes
while True:
    try:
        num_classes = int(input("How many classes did you take this semester? "))
        break # valid input, exit the loop
    except ValueError:
        print("Please enter a valid number.")
         # The loop continues and asks again

# Collect grade and credit info for each class
for i in range(num_classes):
    # Ask for grade first
    while True:
        grade = input(f'Enter grade for class {i+1}: ').upper()
        if grade not in grades:
            print("Invalid grade entered, please enter a valid letter grade (e.g., A, B+, C-).")
        else:
            break # Valid grade entered, exit the inner loop

    
    # Only ask for credits if grade is valid
    while True:
        try:
            credits = float(input(f'Enter credit hours for class {i+1}: '))
            break  # valid credits, exit loop
        except ValueError:
            print("Invalid credit hours. Please enter a number.")

    try:
        calc.add_course(grade, credits)
    except ValueError as e:
        print(e)
        continue

# Calculate and display GPA
gpa = calc.calculator_gpa()
if gpa > 0:
    letter = calc.gpa_to_letter(gpa)
    print(f'Your GPA is: {gpa:.2f} ({letter})')
else:
    print('No valid courses were entered')