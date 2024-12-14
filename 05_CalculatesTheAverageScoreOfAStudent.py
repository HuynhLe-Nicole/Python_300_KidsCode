#The program calculates the average score of a student based on their scores in multiple subjects and then classifies the student into a specific category based on their average score.
#Assumptions: 
#Average score >= 8.5           :   Excellent
#Average score >= 7.0 and < 8.5 :   Good
#Average score >= 5.5 and < 7.0 :   Fair
#Average score >= 4.0 and < 5.5 :   Average
#Average score < 4.0            :   Poor
#Algorithm:
#1. Take input from the user for each subject's score.
#2. Calculate the average score by summing up all the scores and dividing by the number of subjects.
#3. Classify the sudent based on the average score using the classify criteria.
#4. Print out the average score and classification


#Define a function to calculate the average score
def calculate_average(scores):
    return sum(scores) / len(scores)

#Define a function to classify the student
def classify_student(average):
    if average >= 8.5:
        return "Excellent"
    elif average >= 7.0:
        return "Good"
    elif average >= 5.5:
        return "Fair"
    elif average >= 4.0:
        return "Average"
    else:
        return "Poor"
    
#Take input from the user
try:
    scores = []
    num_subjects = int(input("Enter the number of subjects: "))
    if num_subjects <= 0:
        print("Number of subjects must be greater than 0.")
    else:
        for i in range(num_subjects):
            score = float(input(f"Enter score for subject {i+1}: "))
            if score < 0 or score > 10:
                print ("Score must be between 0 and 10. Please try again.")
                break
            scores.append(score)

        if len(scores) == num_subjects:
            average_score = calculate_average(scores)
            classification = classify_student(average_score)
            print(f"Average score: {average_score:.2f}")
            print(f"Classification: {classification}")
except ValueError:
    print("Please enter a valid input.")
