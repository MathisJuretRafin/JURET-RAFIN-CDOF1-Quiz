# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:52:05 2024

@author: MathisJuretRafin
"""

#We create the question according the following template : [Question, Proposition1, Proposition2, Proposition3, Proposition4, Answer]
#Each question has 4 propositions and one answer

question1 = ["What the capital city of France ?", "Paris", "Berlin", "Oslo", "Madrid", "Paris"]
question2 = ["What the capital city of Canada ?", "Ottawa", "Tokyo", "Sydney", "Mexico", "Ottawa"]
question3 = ["What the capital city of Ireland ?", "Berne", "Rome", "Dublin", "Berlin", "Dublin"]
question4 = ["What the capital city of China ?", "Beijing", "Tunis", "Brasilia", "Lisbonne", "Beijing"]
question5 = ["What the capital city of Germany ?", "Paris", "Berlin", "Oslo", "Madrid", "Berlin"]

#We initialize the score variable of our player
score = 0 

#We create a list with all the questions
questionList = [question1,question2,question3,question4,question5]

#This method let the user has a better presentation of the questions
def printQuestion(question):
    result = question[0] + "\n\n"
    for i in question[1:-1]:
        result += i + "\n"
    return result
    

#Let the user answer to the question
for i in questionList:
    print("\n")
    print(printQuestion(i) + "\nEnter your answer :")
    answer = input()
    if(answer == i[5]) : score += 1
print("\n")

#We shiw the result with a personnalized commentary
if(score==0) : print("Your score is ", score, "... You should try to improve your culture")
elif(score >0 and score <4) : print("Your score is ", score, ". You can do better !")
elif(score == 4) : print("Your score is", score, "! Almost perfect !")
else : print("Your score is ", score, "! Perfect !")
    
        
    
    