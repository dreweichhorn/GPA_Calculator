#plan program stucture 

#1. Create a dictionary for grade-to-GPA mapping
#2. Ask how many classes the student took
#3. Loop through each class:
#   - Ask for grade
#   - Ask for credit hours
#   - Convert grade to points
#   - Multiply by credit hours and add to total points
#   - Add credit hours to total credits
#4. Calculate GPA = total_points / total_credits
#5. Display GPA



# dictionary for grades 
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

#create a mapping function for gpa to letter 
def gpa_to_letter(gpa):
    if gpa >= 4.0:
        return "A"
    elif gpa >= 3.7:
        return "A-"
    elif gpa >= 3.3:
        return "B+"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.7:
        return "B-"
    elif gpa >= 2.3:
        return "C+"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.7:
        return "C-"
    elif gpa >= 1.3:
        return "D+"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"

total_points = 0 
total_credits = 0 

# getting info from user on how many classes they took 
num_classes = int(input("The amount of classes taken this semester "))

#you must now loop through the classes 
for i in range(num_classes):
    grade = input(f'Enter grade in class {i+1}: ').upper()
    credit = float(input(f'Enter credit hours for class {i+1}: '))

    if grade not in grades: 
        print('Invalid grade entered, enter correct grade')
        continue

    total_points += grades[grade] * credit
    total_credits += credit

#time to calculate the grade 
if total_credits > 0: 
    gpa = total_points / total_credits
    letter = gpa_to_letter(gpa)
    print(f'Your GPA is: {gpa:.2f}, {letter}')
else:
    ('no valid course was entered')