#------------------------------------------------------------------------
# Program Name: ITS320_CTA4_Option2
# Author: Aliciana Gondick
# Date: Sep. 14, 2023
#------------------------------------------------------------------------
# Pseudocode:
#   1. Input the number of students (between 1 and 30)
#   2. For each student, input their test score
#   3. Compile all scores
#   4. Find the average score 
#   5. Find the highest score
#   6. Find the lowest score
#------------------------------------------------------------------------
# Program inputs: Number of students, test score for each student
# Program Outputs: Average test score, lowest test score, highest test score, sorted scores
#------------------------------------------------------------------------

print("Highest score, lowest score, average score")

Average = 0
HowMany = 0
Counter = 0
Sum = 0
Scores = ""
InputValue = ""
TotalStudents = ""
Grades = []
TestGrades = 0


InputValue = input("How many students? ")
if InputValue == "":
    print("err: Must be a number")
else:
    if not (InputValue.isdigit()):

	    print("err: Must be a number")
    else:
	    HowMany = int(InputValue)
	    if (HowMany < 1) or (HowMany > 30):
		    print("err: Class size is between 1 and 30")
				
			
for i in range(1, HowMany+1):
	Scores = input("Test scores: ")
	Grades.append(Scores)
	Grades.sort()
	if Scores == "":
		print("err: Must be a number")
	else:
		if not (Scores.isdigit()):
			print("err: Must be a number")
		else: 
			Number = int(Scores)
			if (Number > 100) or (Number < 0):
				print("err: Score must be between 0 and 100")
				
	if Number == int(Number):
		Counter = Counter + 1
		Sum = Sum + Number
	
	

TotalStudents = str(HowMany)
TotalStudents.split()


Final= int(TotalStudents)

Average = (Sum)/(Final)
    
print("Student Scores: ",Grades)
print("Average Score is: ", Average)
print("Lowest Score is: ",Grades[0])
print("Highest Score is: ",Grades[-1])
