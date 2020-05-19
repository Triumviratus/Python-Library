#---------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------

def translate(grade):
    value = 0
    grade = grade.upper()
    if grade == "A":
        value = 4.0
    elif grade == "A-":
        value = 3.7
    elif grade == "B+":
        value = 3.3
    elif grade == "B":
        value = 3.0
    elif grade == "B-":
        value = 2.7
    elif grade == "C+":
        value = 2.3
    elif grade == "C":
        value = 2.0
    elif grade == "C-":
        value = 1.7
    elif grade == "D+":
        value = 1.3
    elif grade == "D":
        value = 1.0
    elif grade == "F":
        value = 0.0
    return value

def calcGPA(course_grade, course_credit, number_of_courses):
    y = 0
    z = 0
    for i in range(int(number_of_courses)):
        y += course_grade[i]*course_credit[i]
        z += course_credit[i]
    return (y / z)

def main():
    number_of_courses = input("Enter the number of courses you are currently enrolled in: ")

    while (int(number_of_courses) < 1 or int(number_of_courses) > 7):
        print("Reenter Approximate Value: ")
        number_of_courses = input("Enter the number of courses you are currently enrolled in: ")
    print()

    course_grade = []
    course_credit = []

    for i in range(int(number_of_courses)):
        x = input("Enter grade for course " + str(i+1) + ": ")
        course_grade.append(translate(x))
        course_credit.append(int(input("Enter credits for course " + str(i+1) + ": ")))
        print()

    FinalGPA = calcGPA(course_grade, course_credit, number_of_courses)
    print("Your GPA is " + "%.2f" % FinalGPA)

main()
