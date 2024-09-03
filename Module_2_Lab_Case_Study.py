# kyle mault
# Module_2_Lab_Case_Study.py
# will get a name and a students GPA and see if they made the deans list or Honor roll.
while True:
    last_name = input("Enter the student's last name(or 'ZZZ' to quit): ")

    if last_name == 'ZZZ':
        break
    
    first_name = input("Enter student's first name: ")

    gpa = float(input("Enter student's GPA: "))
        
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")
            
    else:
        print(f"{first_name} {last_name} doesn't qualify for the Dean's List or Honor Roll.")
        break 
